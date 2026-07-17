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
            "[bold blue]AI Settings[/bold blue]",
            border_style="blue"
        )
    )

    table = Table(title="AI Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("AI Engine", "Enabled")
    table.add_row("Verbose Mode", "ON")
    table.add_row("Risk Threshold", "Medium")
    table.add_row("Auto Report", "Enabled")
    table.add_row("YARA Analysis", "Enabled")
    table.add_row("Behavior Analysis", "Enabled")
    table.add_row("Malware Scan", "Enabled")
    table.add_row("Python", platform.python_version())
    table.add_row("Working Directory", os.getcwd())

    console.print(table)

    console.print("\n[bold green]Status[/bold green]")
    console.print("AI configuration loaded successfully.")

    input("\nPress Enter...")
