from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import platform
import os

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]General Settings[/bold green]",
            border_style="green"
        )
    )

    table = Table(title="General Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Framework", "ZCA")
    table.add_row("Version", "0.1 Alpha")
    table.add_row("Python", platform.python_version())
    table.add_row("Platform", platform.system())
    table.add_row("Architecture", platform.machine())
    table.add_row("Working Directory", os.getcwd())
    table.add_row("Reports", "Enabled")
    table.add_row("AI", "Enabled")
    table.add_row("Runtime", "Enabled")
    table.add_row("Theme", "Default")

    console.print(table)

    input("\nPress Enter...")
