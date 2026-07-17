from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Runtime Settings[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Runtime Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Frida Support", "Enabled")
    table.add_row("Memory Scanner", "Enabled")
    table.add_row("SSL Pinning Bypass", "Enabled")
    table.add_row("Root Detection Bypass", "Enabled")
    table.add_row("API Monitor", "Enabled")
    table.add_row("Filesystem Monitor", "Enabled")
    table.add_row("Network Monitor", "Enabled")
    table.add_row("Method Tracer", "Enabled")
    table.add_row("Logcat Monitor", "Enabled")
    table.add_row("Runtime Reports", "Enabled")

    console.print(table)

    input("\nPress Enter...")
