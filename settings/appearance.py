from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Appearance Settings[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Appearance Configuration")

    table.add_column("Option", style="cyan")
    table.add_column("Current Value", style="green")

    table.add_row("Theme", "Default")
    table.add_row("Color Mode", "Bright")
    table.add_row("ASCII Banner", "Enabled")
    table.add_row("Animations", "Enabled")
    table.add_row("Rich Tables", "Enabled")
    table.add_row("Panels", "Enabled")
    table.add_row("Unicode Icons", "Enabled")
    table.add_row("Terminal Width", "Auto")
    table.add_row("Borders", "Rounded")
    table.add_row("Status", "Loaded")

    console.print(table)

    input("\nPress Enter...")
