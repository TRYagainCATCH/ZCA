from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold yellow]Analyzer Settings[/bold yellow]",
            border_style="yellow"
        )
    )

    table = Table(title="Analyzer Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Static Analyzer", "Enabled")
    table.add_row("Runtime Analyzer", "Enabled")
    table.add_row("AI Analyzer", "Enabled")
    table.add_row("APK Information", "Enabled")
    table.add_row("Permission Scan", "Enabled")
    table.add_row("Manifest Scan", "Enabled")
    table.add_row("YARA Scan", "Enabled")
    table.add_row("Malware Detection", "Enabled")
    table.add_row("Auto Analysis", "Disabled")
    table.add_row("Verbose Output", "Enabled")

    console.print(table)

    input("\nPress Enter...")
