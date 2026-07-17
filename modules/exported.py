import zipfile
import re

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]Exported Components Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        with zipfile.ZipFile(apk, "r") as z:
            manifest = z.read("AndroidManifest.xml").decode(
                "utf-8",
                errors="ignore"
            )

        table = Table(title="Exported Components")
        table.add_column("#", style="yellow")
        table.add_column("Component", style="cyan")

        patterns = [
            r'activity[^>]*exported="true"',
            r'service[^>]*exported="true"',
            r'receiver[^>]*exported="true"',
            r'provider[^>]*exported="true"',
        ]

        found = []

        for pattern in patterns:
            found.extend(re.findall(pattern, manifest, re.IGNORECASE))

        if not found:
            console.print("[bold red]No exported components found.[/bold red]")
            input("\nPress Enter...")
            return

        for i, item in enumerate(found, 1):
            table.add_row(str(i), item[:120])

        console.print(table)
        console.print(f"\n[bold cyan]Total:[/bold cyan] {len(found)}")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
