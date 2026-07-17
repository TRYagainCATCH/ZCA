from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def show():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]ZCA Settings Center[/bold cyan]\n"
            "[green]Framework Configuration[/green]",
            border_style="bright_blue"
        )
    )

    table = Table(title="Settings Menu", show_lines=True)

    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Module", style="green")

    modules = [
        "General",
        "Appearance",
        "Analyzer",
        "AI",
        "Runtime",
        "Reports",
        "Updates",
        "Backup",
        "Restore",
        "Plugins",
        "Logs",
        "About"
    ]

    for i, m in enumerate(modules, 1):
        table.add_row(str(i), m)

    table.add_row("0", "Back")

    console.print(table)
