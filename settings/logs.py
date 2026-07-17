from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os
from datetime import datetime

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold yellow]Log Manager[/bold yellow]",
            border_style="yellow"
        )
    )

    os.makedirs("logs", exist_ok=True)

    table = Table(title="Logging Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Logging", "Enabled")
    table.add_row("Log Directory", "logs/")
    table.add_row("Log Level", "INFO")
    table.add_row("Runtime Logs", "Enabled")
    table.add_row("Static Logs", "Enabled")
    table.add_row("AI Logs", "Enabled")
    table.add_row("Error Logs", "Enabled")
    table.add_row("Debug Mode", "Disabled")
    table.add_row("Last Checked", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    console.print(table)

    log_files = os.listdir("logs")

    console.print("\n[bold cyan]Available Log Files[/bold cyan]")

    if log_files:
        for log in log_files:
            console.print(f"• {log}")
    else:
        console.print("[yellow]No log files found.[/yellow]")

    input("\nPress Enter...")
