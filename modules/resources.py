import zipfile
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Resources Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Resources")
    table.add_column("#", style="yellow")
    table.add_column("Resource", style="green")

    count = 1

    try:
        with zipfile.ZipFile(apk) as z:
            for f in z.namelist():
                if f.startswith("res/") or f.startswith("assets/"):
                    table.add_row(str(count), f)
                    count += 1
                    if count > 100:
                        break

        console.print(table)
        console.print(f"\n[bold cyan]Resources Found:[/bold cyan] {count-1}")

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
