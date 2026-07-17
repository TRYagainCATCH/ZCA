from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]AI API Intelligence[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="API Intelligence")

    table.add_column("API", style="cyan")
    table.add_column("Risk", style="yellow")
    table.add_column("AI Analysis", style="green")

    table.add_row("Camera API", "Medium", "Can access device camera.")
    table.add_row("Location API", "High", "Can track user location.")
    table.add_row("Microphone API", "High", "Can record audio.")
    table.add_row("Network API", "Low", "Standard internet communication.")
    table.add_row("Clipboard API", "Medium", "Can read copied text.")
    table.add_row("Bluetooth API", "Low", "Nearby device communication.")
    table.add_row("Biometric API", "Medium", "Uses fingerprint/face authentication.")
    table.add_row("SMS API", "Critical", "Can send or read SMS messages.")

    console.print(table)

    console.print("\n[bold green]AI Recommendation[/bold green]")
    console.print("Review High and Critical APIs to ensure they match the application's expected functionality.")

    input("\nPress Enter...")
