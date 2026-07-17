from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]AI Permission Intelligence[/bold green]",
            border_style="green"
        )
    )

    table = Table(title="Permission Intelligence")

    table.add_column("Permission", style="cyan")
    table.add_column("AI Risk", style="yellow")
    table.add_column("Reason", style="green")

    table.add_row("CAMERA", "Medium", "Can capture images/video")
    table.add_row("RECORD_AUDIO", "High", "Can record microphone")
    table.add_row("ACCESS_FINE_LOCATION", "High", "Tracks precise location")
    table.add_row("READ_CONTACTS", "High", "Accesses contacts")
    table.add_row("READ_SMS", "Critical", "Reads SMS messages")
    table.add_row("INTERNET", "Low", "Required for network access")
    table.add_row("POST_NOTIFICATIONS", "Low", "Displays notifications")
    table.add_row("BLUETOOTH", "Low", "Nearby device communication")

    console.print(table)

    console.print("\n[bold cyan]AI Verdict[/bold cyan]")
    console.print("Sensitive permissions should always be reviewed together with the app's purpose.")

    input("\nPress Enter...")
