from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold blue]AI URL Intelligence[/bold blue]",
            border_style="blue"
        )
    )

    table = Table(title="URL Intelligence")

    table.add_column("URL Type", style="cyan")
    table.add_column("Risk", style="yellow")
    table.add_column("AI Analysis", style="green")

    table.add_row("HTTPS URL", "Low", "Encrypted connection.")
    table.add_row("HTTP URL", "High", "Unencrypted communication.")
    table.add_row("IP Address URL", "Medium", "Review destination.")
    table.add_row("Firebase URL", "Low", "Backend service.")
    table.add_row("REST API", "Low", "Standard API endpoint.")
    table.add_row("WebSocket", "Medium", "Persistent connection.")
    table.add_row("Short URL", "High", "Destination should be verified.")
    table.add_row("Unknown Domain", "Medium", "Requires manual review.")

    console.print(table)

    console.print("\n[bold green]AI Recommendation[/bold green]")
    console.print("Prefer HTTPS endpoints and investigate unknown or shortened URLs before trusting them.")

    input("\nPress Enter...")
