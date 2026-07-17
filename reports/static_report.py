from rich.console import Console
from rich.panel import Panel
import glob
import os

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]Static Reports[/bold green]",
            border_style="green"
        )
    )

    files = sorted(glob.glob("*.txt"))

    if not files:
        console.print("[red]No static reports found.[/red]")
    else:
        for i, f in enumerate(files, 1):
            size = os.path.getsize(f)
            console.print(f"[cyan]{i:02}[/cyan] {f}  ({size} bytes)")

    input("\nPress Enter...")
