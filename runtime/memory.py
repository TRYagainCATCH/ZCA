from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Memory Scanner[/bold cyan]",
            border_style="cyan"
        )
    )

    console.print("[green]✔ Runtime Memory Scanner[/green]\n")
    console.print("• Heap Analysis")
    console.print("• Native Memory")
    console.print("• Java Objects")
    console.print("• Memory Dump")
    console.print("• Memory Leak Detection")

    input("\nPress Enter...")
