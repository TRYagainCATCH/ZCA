from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold magenta]Plugin Manager[/bold magenta]",
            border_style="magenta"
        )
    )

    table = Table(title="Installed Plugins")

    table.add_column("Plugin", style="cyan")
    table.add_column("Status", style="green")

    table.add_row("Static Analyzer", "Loaded")
    table.add_row("Runtime Analyzer", "Loaded")
    table.add_row("AI Analyzer", "Loaded")
    table.add_row("YARA Engine", "Loaded")
    table.add_row("Frida Runtime", "Optional")
    table.add_row("APKTool", "Loaded")
    table.add_row("JADX", "Loaded")
    table.add_row("Androguard", "Loaded")
    table.add_row("Future Plugins", "Supported")

    console.print(table)

    input("\nPress Enter...")
