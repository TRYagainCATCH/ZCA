from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold yellow]Logcat Monitor[/bold yellow]",
            border_style="yellow"
        )
    )

    console.print("[bold green]Android Logcat Analyzer[/bold green]\n")

    logs = [
        "System Logs",
        "Application Logs",
        "Crash Logs",
        "Exception Monitor",
        "ANR Detection",
        "Security Logs",
        "Network Logs",
        "Activity Lifecycle",
        "Service Lifecycle",
        "Broadcast Events",
        "Content Provider Logs",
        "Export Log Report"
    ]

    for i, item in enumerate(logs, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {item}")

    input("\nPress Enter...")
