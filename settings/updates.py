from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import platform

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold yellow]Update Settings[/bold yellow]",
            border_style="yellow"
        )
    )

    table = Table(title="Update Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Current Version", "0.1 Alpha")
    table.add_row("Update Channel", "Stable")
    table.add_row("Auto Check", "Enabled")
    table.add_row("Auto Download", "Disabled")
    table.add_row("Notify on Update", "Enabled")
    table.add_row("Last Check", "Never")
    table.add_row("Internet Required", "Yes")
    table.add_row("Platform", platform.system())
    table.add_row("Status", "Up to Date")

    console.print(table)

    input("\nPress Enter...")
