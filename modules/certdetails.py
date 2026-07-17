import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Certificate Details[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Signing Certificate")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    try:
        output = subprocess.check_output(
            ["apksigner", "verify", "--print-certs", apk],
            text=True
        )

        for line in output.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                table.add_row(k.strip(), v.strip())

        console.print(table)

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
