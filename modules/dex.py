import zipfile

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]DEX Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        with zipfile.ZipFile(apk, "r") as z:
            files = z.namelist()

            dex = [f for f in files if f.endswith(".dex")]

            if not dex:
                console.print("[bold red]No DEX files found.[/bold red]")
                input("\nPress Enter...")
                return

            table = Table(title="DEX Files")
            table.add_column("#", style="yellow")
            table.add_column("DEX File", style="green")
            table.add_column("Size", style="cyan")

            for i, f in enumerate(dex, 1):
                size = z.getinfo(f).file_size
                table.add_row(
                    str(i),
                    f,
                    f"{round(size/1024/1024,2)} MB"
                )

            console.print(table)
            console.print(f"\n[bold cyan]Total DEX Files:[/bold cyan] {len(dex)}")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
