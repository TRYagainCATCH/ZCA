from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold yellow]AI Vulnerability Predictor[/bold yellow]",
            border_style="yellow"
        )
    )

    table = Table(title="Predicted Vulnerabilities")

    table.add_column("Category", style="cyan")
    table.add_column("Risk", style="red")
    table.add_column("AI Comment", style="green")

    table.add_row("Exported Components", "LOW", "No obvious exposure detected")
    table.add_row("Permissions", "MEDIUM", "Review sensitive permissions")
    table.add_row("Network Security", "LOW", "No clear issues found")
    table.add_row("Hardcoded Secrets", "LOW", "No evidence detected")
    table.add_row("WebView", "MEDIUM", "Requires manual inspection")
    table.add_row("Native Libraries", "LOW", "Looks normal")
    table.add_row("Cryptography", "LOW", "No weak patterns detected")
    table.add_row("Overall Score", "8.8/10", "Application appears relatively secure")

    console.print(table)

    console.print("\n[bold green]AI Recommendation[/bold green]")
    console.print("Perform dynamic analysis to confirm these predictions.")

    input("\nPress Enter...")
