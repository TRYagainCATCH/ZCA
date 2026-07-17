from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os
import platform

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold blue]Reports Settings[/bold blue]",
            border_style="blue"
        )
    )

    table = Table(title="Reports Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Auto Save", "Enabled")
    table.add_row("Output Folder", os.getcwd())
    table.add_row("Default Format", "TXT")
    table.add_row("PDF Export", "Enabled")
    table.add_row("HTML Export", "Enabled")
    table.add_row("JSON Export", "Enabled")
    table.add_row("History", "Enabled")
    table.add_row("Platform", platform.system())
    table.add_row("Python", platform.python_version())

    console.print(table)

    input("\nPress Enter...")
