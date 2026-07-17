import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Certificate Verification[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        subprocess.check_output(
            ["apksigner", "verify", apk],
            stderr=subprocess.STDOUT,
            text=True
        )

        console.print("[bold green]✓ APK Signature is VALID[/bold green]")

    except subprocess.CalledProcessError as e:
        console.print("[bold red]✗ APK Signature is INVALID[/bold red]")
        console.print(e.output)

    input("\nPress Enter...")
