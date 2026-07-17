import subprocess
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Application Components[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        out = subprocess.check_output(
            ["aapt", "dump", "badging", apk],
            text=True
        )

        table = Table(title="Components")
        table.add_column("Type", style="cyan")
        table.add_column("Name", style="green")

        for line in out.splitlines():

            if line.startswith("launchable-activity:"):
                table.add_row(
                    "Launcher Activity",
                    line.split("name='")[1].split("'")[0]
                )

            elif line.startswith("package:"):
                table.add_row(
                    "Package",
                    line.split("name='")[1].split("'")[0]
                )

            elif line.startswith("application-label:"):
                table.add_row(
                    "Application",
                    line.split("'")[1]
                )

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
