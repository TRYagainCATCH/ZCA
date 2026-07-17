from rich.console import Console
from rich.panel import Panel
import glob
import os

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold magenta]AI Reports[/bold magenta]",
            border_style="magenta"
        )
    )

    files = sorted(glob.glob("ai_report*.txt"))

    if not files:
        console.print("[red]No AI reports found.[/red]")
    else:
        for i, f in enumerate(files, 1):
            size = os.path.getsize(f)
            console.print(f"[cyan]{i:02}[/cyan] {f} ({size} bytes)")

    input("\nPress Enter...")
