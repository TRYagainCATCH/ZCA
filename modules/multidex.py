import zipfile
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Multi DEX Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="DEX Files")
    table.add_column("#", style="yellow")
    table.add_column("DEX File", style="green")
    table.add_column("Size", style="cyan")

    count = 1

    try:
        with zipfile.ZipFile(apk) as z:
            dex = [f for f in z.namelist() if f.endswith(".dex")]

            for f in dex:
                size = len(z.read(f)) // 1024
                table.add_row(str(count), f, f"{size} KB")
                count += 1

            console.print(table)
            console.print(f"\n[bold green]Total DEX Files:[/bold green] {len(dex)}")

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
