from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold yellow]JavaScript Injector[/bold yellow]",
            border_style="yellow"
        )
    )

    console.print("[bold green]JavaScript Runtime Toolkit[/bold green]\n")

    modules = [
        "Inject JavaScript",
        "Hook Java Methods",
        "Hook Native Methods",
        "Trace Function Calls",
        "Modify Return Values",
        "Monitor Arguments",
        "Bypass SSL Pinning",
        "Dump Runtime Objects",
        "Enumerate Classes",
        "Enumerate Methods",
        "Spawn Script",
        "Live Console"
    ]

    for i, m in enumerate(modules, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {m}")

    input("\nPress Enter...")
