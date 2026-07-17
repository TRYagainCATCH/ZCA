from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datetime import datetime

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]Restore Settings[/bold green]",
            border_style="green"
        )
    )

    table = Table(title="Restore Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Restore Status", "Enabled")
    table.add_row("Restore Source", "backups/")
    table.add_row("Configuration", "Supported")
    table.add_row("Reports", "Supported")
    table.add_row("Logs", "Supported")
    table.add_row("Plugins", "Supported")
    table.add_row("Verify Backup", "Enabled")
    table.add_row("Overwrite Files", "Disabled")
    table.add_row("Last Restore", "Never")
    table.add_row("Current Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    console.print(table)

    input("\nPress Enter...")
