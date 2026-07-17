from rich.console import Console
from rich.panel import Panel
import subprocess

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Frida Manager[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        version = subprocess.check_output(
            ["frida", "--version"],
            text=True
        ).strip()

        console.print(f"[green]✓ Frida Installed[/green]")
        console.print(f"[cyan]Version:[/cyan] {version}")

    except:
        console.print("[red]✗ Frida is not installed[/red]")
        console.print("[yellow]pkg install frida-tools[/yellow]")

    input("\nPress Enter...")
