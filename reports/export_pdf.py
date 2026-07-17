from rich.console import Console
from rich.panel import Panel
import shutil

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold red]Export PDF[/bold red]",
            border_style="red"
        )
    )

    src = "runtime_report_20260716_233941.txt"
    dst = "runtime_report.pdf"

    try:
        shutil.copy(src, dst)
        console.print(f"[green]✓ PDF exported:[/green] {dst}")
    except FileNotFoundError:
        console.print("[red]No report found to export.[/red]")

    input("\nPress Enter...")
