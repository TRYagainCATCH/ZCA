import os

from rich.console import Console
from rich.panel import Panel

console = Console()

def run(apk):
    os.system("clear")

    console.print(
        Panel.fit(
            "[bold cyan]Certificate Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    os.system(f'apksigner verify --print-certs "{apk}"')

    input("\nPress Enter...")
