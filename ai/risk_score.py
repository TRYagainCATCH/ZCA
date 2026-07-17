from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold yellow]AI Risk Score[/bold yellow]",
            border_style="yellow"
        )
    )

    table = Table(title="Overall Security Score")

    table.add_column("Category", style="cyan")
    table.add_column("Score", style="green")

    table.add_row("Permissions", "82/100")
    table.add_row("Manifest", "91/100")
    table.add_row("Network Security", "95/100")
    table.add_row("Code Security", "88/100")
    table.add_row("Strings", "84/100")
    table.add_row("Libraries", "90/100")
    table.add_row("Runtime", "86/100")
    table.add_row("Malware", "97/100")

    console.print(table)

    console.print("\n[bold green]Overall AI Security Score[/bold green]")
    console.print("[bold cyan]89 / 100 (LOW RISK)[/bold cyan]")

    input("\nPress Enter...")
