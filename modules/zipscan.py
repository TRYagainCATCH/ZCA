import zipfile
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(apk_path):
    console.print(
        Panel.fit(
            "[bold cyan]APK ZIP Explorer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        with zipfile.ZipFile(apk_path, "r") as apk:
            table = Table(title="APK Contents (First 30 Files)")
            table.add_column("#", style="yellow")
            table.add_column("File", style="green")

            files = apk.namelist()

            for i, f in enumerate(files[:30], 1):
                table.add_row(str(i), f)

            console.print(table)
            console.print(f"\n[bold green]Total Files:[/bold green] {len(files)}")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

    input("\nPress Enter...")
