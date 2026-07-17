from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold blue]AI Security Recommendations[/bold blue]",
            border_style="blue"
        )
    )

    table = Table(title="Recommendations")

    table.add_column("#", style="cyan", justify="center")
    table.add_column("Recommendation", style="green")

    recommendations = [
        "Review all Dangerous permissions.",
        "Use HTTPS for all network traffic.",
        "Enable certificate pinning.",
        "Remove hardcoded secrets and API keys.",
        "Obfuscate release builds using R8/ProGuard.",
        "Verify APK signature before installation.",
        "Perform runtime analysis with Frida.",
        "Scan APK using YARA rules.",
        "Check exported components.",
        "Review native libraries.",
        "Inspect suspicious strings.",
        "Perform manual reverse engineering."
    ]

    for i, rec in enumerate(recommendations, 1):
        table.add_row(str(i), rec)

    console.print(table)

    console.print("\n[bold green]AI Advice[/bold green]")
    console.print("Follow these recommendations to improve the overall security assessment of the application.")

    input("\nPress Enter...")
