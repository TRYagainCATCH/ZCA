from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold yellow]Anti Emulator Detector[/bold yellow]",
            border_style="yellow"
        )
    )

    console.print("[green]✔ Emulator Detection Checks[/green]\n")

    checks = [
        "Build Fingerprint",
        "Generic Device",
        "QEMU Detection",
        "Goldfish Hardware",
        "Ranchu Hardware",
        "Genymotion Detection",
        "Android SDK Emulator",
        "Virtual Sensors",
        "Emulator Files",
        "Emulator Properties"
    ]

    for i, c in enumerate(checks, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {c}")

    input("\nPress Enter...")
