import zipfile

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]Assets Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        with zipfile.ZipFile(apk, "r") as z:
            files = z.namelist()

            assets = [f for f in files if f.startswith("assets/")]

            if not assets:
                console.print("[bold red]No assets found.[/bold red]")
                input("\nPress Enter...")
                return

            table = Table(title="Assets")
            table.add_column("#", style="yellow")
            table.add_column("Asset", style="green")

            for i, asset in enumerate(assets[:200], 1):
                table.add_row(str(i), asset)

            console.print(table)
            console.print(f"\n[bold cyan]Total Assets:[/bold cyan] {len(assets)}")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
