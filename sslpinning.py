from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]SSL Pinning Bypass[/bold cyan]",
            border_style="cyan"
        )
    )

    console.print("[green]✔ SSL Pinning Analysis[/green]\n")
    console.print("• Detect SSL Pinning")
    console.print("• TrustManager Hooks")
    console.print("• OkHttp Detection")
    console.print("• Certificate Pinning")
    console.print("• Bypass Status")

    input("\nPress Enter...")
