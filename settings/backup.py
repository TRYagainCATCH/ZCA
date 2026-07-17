from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datetime import datetime

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold blue]Backup Settings[/bold blue]",
            border_style="blue"
        )
    )

    table = Table(title="Backup Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Backup Status", "Enabled")
    table.add_row("Backup Location", "backups/")
    table.add_row("Auto Backup", "Disabled")
    table.add_row("Backup Format", "ZIP")
    table.add_row("Configuration", "Included")
    table.add_row("Reports", "Included")
    table.add_row("Logs", "Included")
    table.add_row("Plugins", "Included")
    table.add_row("Last Backup", "Never")
    table.add_row("Current Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    console.print(table)

    input("\nPress Enter...")
