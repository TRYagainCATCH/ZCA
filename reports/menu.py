from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def show():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]ZCA Reports Center[/bold cyan]\n"
            "[green]Generate & Export Analysis Reports[/green]",
            border_style="bright_blue"
        )
    )

    table = Table(title="Reports Menu", show_lines=True)

    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Module", style="green")

    modules = [
        "Static Report",
        "Runtime Report",
        "AI Report",
        "Final Report",
        "Export PDF",
        "Export HTML",
        "Export JSON",
        "History",
        "Settings"
    ]

    for i, m in enumerate(modules, 1):
        table.add_row(str(i), m)

    table.add_row("0", "Back")

    console.print(table)
