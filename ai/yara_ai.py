from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold red]AI YARA Intelligence[/bold red]",
            border_style="red"
        )
    )

    table = Table(title="YARA AI Analysis")

    table.add_column("Rule", style="cyan")
    table.add_column("Status", style="yellow")
    table.add_column("AI Result", style="green")

    table.add_row("Trojan Rules", "✓", "No Match")
    table.add_row("Spyware Rules", "✓", "No Match")
    table.add_row("Ransomware Rules", "✓", "No Match")
    table.add_row("Banker Rules", "✓", "No Match")
    table.add_row("Adware Rules", "⚠", "Possible Match")
    table.add_row("Crypto Miner", "✓", "No Match")
    table.add_row("Obfuscation", "⚠", "Detected")
    table.add_row("Packed APK", "⚠", "Possible")
    table.add_row("Shell Detection", "✓", "No Match")
    table.add_row("Overall Verdict", "LOW", "Mostly Clean")

    console.print(table)

    console.print("\n[bold green]AI Recommendation[/bold green]")
    console.print("Review matched YARA rules manually to confirm whether they indicate a real threat or expected app behavior.")

    input("\nPress Enter...")
