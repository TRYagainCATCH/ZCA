from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import platform
import sys

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]About ZCA[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="ZCA Framework Information")

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Framework", "ZCA - Zed Code Analyzer")
    table.add_row("Version", "0.1 Alpha")
    table.add_row("Developer", "Zabiullah")
    table.add_row("Language", "Python")
    table.add_row("Platform", platform.system())
    table.add_row("Architecture", platform.machine())
    table.add_row("Python", sys.version.split()[0])
    table.add_row("Static Modules", "20+")
    table.add_row("Runtime Modules", "16")
    table.add_row("AI Modules", "15")
    table.add_row("Reports", "9")
    table.add_row("License", "MIT (Planned)")

    console.print(table)

    console.print(
        Panel(
            "[bold green]ZCA[/bold green] is an Android APK security analysis framework "
            "designed for Static Analysis, Runtime Analysis, AI-powered Analysis, "
            "and Professional Report Generation.",
            title="Description",
            border_style="green"
        )
    )

    input("\nPress Enter...")
