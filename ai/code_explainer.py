from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]AI Code Explainer[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Code Analysis")

    table.add_column("Component", style="cyan")
    table.add_column("AI Explanation", style="green")

    table.add_row("Activity", "Controls application screens.")
    table.add_row("Service", "Runs background operations.")
    table.add_row("BroadcastReceiver", "Receives system events.")
    table.add_row("ContentProvider", "Shares application data.")
    table.add_row("Native Library", "Contains compiled native code.")
    table.add_row("DEX", "Stores Dalvik bytecode.")
    table.add_row("Manifest", "Defines app configuration.")
    table.add_row("Permission", "Requests Android capabilities.")

    console.print(table)

    console.print("\n[bold yellow]AI Summary[/bold yellow]")
    console.print("The application structure appears normal and follows standard Android architecture.")

    input("\nPress Enter...")
