import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Deep Manifest Viewer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        output = subprocess.check_output(
            ["aapt", "dump", "xmltree", apk, "AndroidManifest.xml"],
            text=True
        )
        console.print(output)
    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
