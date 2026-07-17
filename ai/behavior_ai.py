from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]AI Behavior Analysis[/bold green]",
            border_style="green"
        )
    )

    table = Table(title="Behavior Intelligence")

    table.add_column("Behavior", style="cyan")
    table.add_column("Risk", style="yellow")
    table.add_column("AI Assessment", style="green")

    table.add_row("Background Services", "Medium", "Runs continuously.")
    table.add_row("Boot Receiver", "Medium", "Starts after device boot.")
    table.add_row("Network Activity", "Low", "Normal communication.")
    table.add_row("Location Access", "High", "Tracks user location.")
    table.add_row("Camera Usage", "Medium", "Uses camera hardware.")
    table.add_row("Microphone Usage", "High", "Records audio.")
    table.add_row("Clipboard Access", "Medium", "Reads copied content.")
    table.add_row("File Operations", "Low", "Reads/Writes application files.")
    table.add_row("Dynamic Code Loading", "Critical", "May execute downloaded code.")
    table.add_row("Reflection Usage", "Medium", "Can hide functionality.")

    console.print(table)

    console.print("\n[bold cyan]AI Verdict[/bold cyan]")
    console.print("Behavior appears normal unless Critical indicators are confirmed during runtime analysis.")

    input("\nPress Enter...")
