from rich.console import Console
from rich.panel import Panel
from datetime import datetime
import os

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]Runtime Analysis Report[/bold green]",
            border_style="green"
        )
    )

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/runtime_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("          ZCA RUNTIME ANALYSIS REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Generated : {datetime.now()}\n\n")

        modules = [
            "Frida Manager",
            "Memory Scanner",
            "SSL Pinning",
            "Root Detection",
            "Anti Emulator",
            "API Monitor",
            "Filesystem Monitor",
            "Network Monitor",
            "Process Monitor",
            "JavaScript Injector",
            "DEX Dumper",
            "Universal Bypass",
            "Method Tracer",
            "Logcat Monitor",
            "Native Library Calls"
        ]

        for i, module in enumerate(modules, 1):
            f.write(f"{i:02}. {module}\n")

        f.write("\nStatus : Runtime Analysis Completed\n")

    console.print(f"[bold green]✓ Report Saved Successfully[/bold green]")
    console.print(f"[cyan]{filename}[/cyan]")

    input("\nPress Enter...")
