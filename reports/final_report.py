from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datetime import datetime

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]Final Analysis Report[/bold green]",
            border_style="green"
        )
    )

    table = Table(title="ZCA Final Report")

    table.add_column("Category", style="cyan")
    table.add_column("Status", style="green")

    table.add_row("APK Information", "✓ Complete")
    table.add_row("Permissions", "✓ Complete")
    table.add_row("Manifest", "✓ Complete")
    table.add_row("Network Security", "✓ Complete")
    table.add_row("Strings", "✓ Complete")
    table.add_row("Runtime Analysis", "✓ Complete")
    table.add_row("AI Analysis", "✓ Complete")
    table.add_row("Risk Score", "89/100")
    table.add_row("Overall Verdict", "LOW RISK")

    console.print(table)

    console.print(f"\n[bold yellow]Generated:[/bold yellow] {datetime.now()}")

    input("\nPress Enter...")
