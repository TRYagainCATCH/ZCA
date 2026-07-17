from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold magenta]Process Monitor[/bold magenta]",
            border_style="magenta"
        )
    )

    console.print("[bold green]Runtime Process Analysis[/bold green]\n")

    processes = [
        "Running Processes",
        "Spawned Processes",
        "Child Processes",
        "Thread Monitor",
        "PID Information",
        "Foreground Process",
        "Background Services",
        "Loaded Libraries",
        "Memory Usage",
        "CPU Usage",
        "JNI Processes",
        "System Processes"
    ]

    for i, p in enumerate(processes, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {p}")

    input("\nPress Enter...")
