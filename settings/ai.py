from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold magenta]AI Settings[/bold magenta]",
            border_style="magenta"
        )
    )

    table = Table(title="AI Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("AI Engine", "Enabled")
    table.add_row("Malware Detection", "Enabled")
    table.add_row("Risk Prediction", "Enabled")
    table.add_row("Behavior Analysis", "Enabled")
    table.add_row("YARA AI", "Enabled")
    table.add_row("Code Explainer", "Enabled")
    table.add_row("Auto Recommendations", "Enabled")
    table.add_row("AI Report", "Enabled")
    table.add_row("Confidence Level", "High")
    table.add_row("Model", "ZCA AI Engine v0.1")

    console.print(table)

    input("\nPress Enter...")
