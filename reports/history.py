from rich.console import Console
from rich.panel import Panel
import glob
import os

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Report History[/bold cyan]",
            border_style="cyan"
        )
    )

    files = sorted(glob.glob("*.txt") + glob.glob("*.json") + glob.glob("*.html"))

    if not files:
        console.print("[red]No reports found.[/red]")
    else:
        for i, file in enumerate(files, 1):
            size = os.path.getsize(file)
            console.print(f"[cyan]{i:02}[/cyan] {file} ({size} bytes)")

    input("\nPress Enter...")
