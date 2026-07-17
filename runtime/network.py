from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold blue]Network Monitor[/bold blue]",
            border_style="blue"
        )
    )

    console.print("[bold green]Runtime Network Analysis[/bold green]\n")

    items = [
        "HTTP Requests",
        "HTTPS Requests",
        "DNS Queries",
        "TCP Connections",
        "UDP Connections",
        "WebSocket Traffic",
        "SSL/TLS Sessions",
        "Downloaded Files",
        "Uploaded Files",
        "IP Addresses",
        "Domains",
        "Certificate Validation"
    ]

    for i, item in enumerate(items, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {item}")

    input("\nPress Enter...")

