from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]Reports Settings[/bold green]",
            border_style="green"
        )
    )

    table = Table(title="Reports Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Auto Save Reports", "Enabled")
    table.add_row("Generate TXT", "Enabled")
    table.add_row("Generate HTML", "Enabled")
    table.add_row("Generate JSON", "Enabled")
    table.add_row("Generate PDF", "Enabled")
    table.add_row("Report History", "Enabled")
    table.add_row("Compression", "Disabled")
    table.add_row("Overwrite Existing", "Disabled")
    table.add_row("Timestamp", "Enabled")
    table.add_row("Export Directory", "reports/")

    console.print(table)

    input("\nPress Enter...")
