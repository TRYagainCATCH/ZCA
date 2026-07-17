import zipfile
import re

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]Code Obfuscation Detector[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        with zipfile.ZipFile(apk, "r") as z:
            names = z.namelist()

        patterns = [
            r"/a\.class$",
            r"/b\.class$",
            r"/c\.class$",
            r"/aa\.class$",
            r"/ab\.class$",
            r"/ac\.class$",
            r"/[a-z]{1,2}\.dex$",
        ]

        results = []

        for f in names:
            for p in patterns:
                if re.search(p, f):
                    results.append(f)
                    break

        table = Table(title="Obfuscation Results")
        table.add_column("#", style="yellow")
        table.add_column("Matched File", style="green")

        if results:
            for i, item in enumerate(sorted(set(results)), 1):
                table.add_row(str(i), item)

            console.print(table)
            console.print(
                f"\n[bold red]Possible Obfuscation Detected[/bold red] ({len(set(results))} matches)"
            )
        else:
            console.print("[bold green]No obvious obfuscation detected.[/bold green]")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
