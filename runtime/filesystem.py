from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]Filesystem Monitor[/bold green]",
            border_style="green"
        )
    )

    console.print("[bold cyan]Runtime Filesystem Analysis[/bold cyan]\n")

    items = [
        "Open Files",
        "Read Operations",
        "Write Operations",
        "Delete Operations",
        "Shared Preferences",
        "SQLite Databases",
        "Cache Files",
        "External Storage Access",
        "Internal Storage Access",
        "Temporary Files",
        "Hidden Files",
        "Sensitive File Access"
    ]

    for i, item in enumerate(items, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {item}")

    input("\nPress Enter...")
