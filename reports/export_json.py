from rich.console import Console
from rich.panel import Panel
import json

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold yellow]Export JSON[/bold yellow]",
            border_style="yellow"
        )
    )

    report = {
        "project": "ZCA",
        "version": "0.1 Alpha",
        "analysis": {
            "static": "Completed",
            "runtime": "Completed",
            "ai": "Completed"
        },
        "risk_score": 89,
        "verdict": "LOW RISK"
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    console.print("[green]✓ JSON report exported successfully[/green]")
    console.print("[cyan]report.json[/cyan]")

    input("\nPress Enter...")
