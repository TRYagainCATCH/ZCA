from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import platform
import sys

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold magenta]AI Model Information[/bold magenta]",
            border_style="magenta"
        )
    )

    table = Table(title="AI Engine Information")

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Engine", "ZCA AI Engine")
    table.add_row("Version", "0.1 Alpha")
    table.add_row("Analysis Mode", "Static + Runtime + AI")
    table.add_row("Malware Detection", "Enabled")
    table.add_row("Risk Prediction", "Enabled")
    table.add_row("YARA AI", "Enabled")
    table.add_row("Python", sys.version.split()[0])
    table.add_row("Platform", platform.system())
    table.add_row("Architecture", platform.machine())

    console.print(table)

    console.print("\n[bold green]Status[/bold green]")
    console.print("AI Engine initialized successfully.")

    input("\nPress Enter...")
