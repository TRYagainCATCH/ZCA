import subprocess
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]SDK Information[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        out = subprocess.check_output(
            ["aapt", "dump", "badging", apk],
            text=True
        )

        sdk = "-"
        target = "-"
        version = "-"
        package = "-"

        for line in out.splitlines():

            if line.startswith("package:"):
                package = line.split("name='")[1].split("'")[0]

            elif "sdkVersion:" in line:
                sdk = line.split("'")[1]

            elif "targetSdkVersion:" in line:
                target = line.split("'")[1]

            elif "versionName=" in line:
                version = line.split("versionName='")[1].split("'")[0]

        table = Table(title="SDK Information")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Package", package)
        table.add_row("Version", version)
        table.add_row("Min SDK", sdk)
        table.add_row("Target SDK", target)

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
