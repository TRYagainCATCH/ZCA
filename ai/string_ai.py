from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold magenta]AI String Intelligence[/bold magenta]",
            border_style="magenta"
        )
    )

    table = Table(title="String Intelligence")

    table.add_column("String Type", style="cyan")
    table.add_column("Risk", style="yellow")
    table.add_column("AI Analysis", style="green")

    table.add_row("URLs", "Medium", "External communication detected.")
    table.add_row("IP Addresses", "Medium", "Review hardcoded IPs.")
    table.add_row("API Keys", "High", "Potential sensitive information.")
    table.add_row("JWT Tokens", "Critical", "Authentication tokens found.")
    table.add_row("Firebase URLs", "Low", "Cloud backend references.")
    table.add_row("Emails", "Low", "Developer contact information.")
    table.add_row("Passwords", "Critical", "Possible hardcoded credentials.")
    table.add_row("File Paths", "Low", "Internal application paths.")

    console.print(table)

    console.print("\n[bold green]AI Verdict[/bold green]")
    console.print("Review Critical strings carefully before trusting the application.")

    input("\nPress Enter...")
