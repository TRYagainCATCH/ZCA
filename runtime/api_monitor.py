from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]API Monitor[/bold cyan]",
            border_style="cyan"
        )
    )

    console.print("[green]✔ API Monitoring Module[/green]\n")

    apis = [
        "Java API Calls",
        "JNI Calls",
        "Reflection API",
        "Crypto API",
        "File API",
        "Network API",
        "Clipboard API",
        "Location API",
        "Camera API",
        "Microphone API",
        "SMS API",
        "Contacts API"
    ]

    for i, api in enumerate(apis, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {api}")

    input("\nPress Enter...")
