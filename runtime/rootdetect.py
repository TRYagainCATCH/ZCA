from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold red]Root Detection Bypass[/bold red]",
            border_style="red"
        )
    )

    console.print("[green]✔ Root Detection Analysis[/green]\n")

    checks = [
        "su Binary Check",
        "Magisk Detection",
        "BusyBox Detection",
        "Test-Keys Check",
        "RW System Partition",
        "Root Apps Detection",
        "Frida Hook Ready"
    ]

    for i, c in enumerate(checks, 1):
        console.print(f"[cyan]{i}.[/cyan] {c}")

    input("\nPress Enter...")
