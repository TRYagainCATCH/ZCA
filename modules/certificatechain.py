import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Certificate Chain Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        output = subprocess.check_output(
            ["apksigner", "verify", "--print-certs", "--verbose", apk],
            text=True
        )

        console.print(output)

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
