from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def show():
    console.clear()

    console.print(
        Panel.fit(
            """
[bold bright_cyan]
██████╗ ██╗   ██╗███╗   ██╗████████╗██╗███╗   ███╗███████╗
██╔══██╗██║   ██║████╗  ██║╚══██╔══╝██║████╗ ████║██╔════╝
██████╔╝██║   ██║██╔██╗ ██║   ██║   ██║██╔████╔██║█████╗
██╔══██╗██║   ██║██║╚██╗██║   ██║   ██║██║╚██╔╝██║██╔══╝
██║  ██║╚██████╔╝██║ ╚████║   ██║   ██║██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝
[/bold bright_cyan]

        ★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★
               ANDROID RUNTIME ANALYZER
        ★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★
""",
            border_style="bright_blue",
            title="[bold green]ZCA Runtime[/bold green]"
        )
    )

    table = Table(
        title="[bold yellow]Runtime Modules[/bold yellow]",
        border_style="bright_blue",
        show_lines=True
    )

    table.add_column("ID", justify="center", style="cyan", width=5)
    table.add_column("Module", style="green")

    table.add_row("1", "Frida Manager")
    table.add_row("2", "Memory Scanner")
    table.add_row("3", "SSL Pinning Bypass")
    table.add_row("4", "Root Detection Bypass")
    table.add_row("5", "Anti Emulator")
    table.add_row("6", "API Monitor")
    table.add_row("7", "Filesystem Monitor")
    table.add_row("8", "Network Monitor")
    table.add_row("9", "Process Monitor")
    table.add_row("10", "JavaScript Injector")
    table.add_row("11", "Dump DEX")
    table.add_row("12", "Universal Bypass")
    table.add_row("13", "Method Tracer")
    table.add_row("14", "Logcat Monitor")
    table.add_row("15", "Native Lib Calls")
    table.add_row("16", "Runtime Report")
    table.add_row("0", "Back")

    console.print(table)
