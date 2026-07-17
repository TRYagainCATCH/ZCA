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
 █████╗ ██╗
██╔══██╗██║
███████║██║
██╔══██║██║
██║  ██║██║
╚═╝  ╚═╝╚═╝

      ★ AI ANALYZER ★
 Android Intelligence Engine
[/bold bright_cyan]
""",
            border_style="bright_blue",
            title="[bold green]ZCA AI[/bold green]"
        )
    )

    table = Table(title="AI Modules", show_lines=True)

    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Module", style="green")

    modules = [
        "AI Malware Detection",
        "Code Explainer",
        "Vulnerability Predictor",
        "Permission AI",
        "API Intelligence",
        "String Intelligence",
        "URL Intelligence",
        "Behavior Analysis",
        "YARA AI",
        "Risk Score",
        "AI Summary",
        "AI Report",
        "Recommendations",
        "Model Information",
        "Settings"
    ]

    for i, m in enumerate(modules, 1):
        table.add_row(str(i), m)

    table.add_row("0", "Back")

    console.print(table)
