from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]DEX Dumper[/bold cyan]",
            border_style="cyan"
        )
    )

    console.print("[bold green]DEX Runtime Dump Module[/bold green]\n")

    items = [
        "Dump classes.dex",
        "Dump classes2.dex",
        "Dump classes3.dex",
        "Extract In-Memory DEX",
        "Detect Packed APK",
        "Dump Optimized DEX",
        "Verify DEX Header",
        "DEX Size",
        "DEX Checksum",
        "DEX Strings",
        "DEX Methods",
        "Save Dump Report"
    ]

    for i, item in enumerate(items, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {item}")

    input("\nPress Enter...")
