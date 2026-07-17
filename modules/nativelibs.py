import zipfile

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]Native Libraries Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        with zipfile.ZipFile(apk, "r") as z:
            files = z.namelist()

            libs = [f for f in files if f.startswith("lib/") and f.endswith(".so")]

            if not libs:
                console.print("[bold red]No native libraries found.[/bold red]")
                input("\nPress Enter...")
                return

            table = Table(title="Native Libraries")
            table.add_column("#", style="yellow")
            table.add_column("Architecture", style="cyan")
            table.add_column("Library", style="green")

            for i, lib in enumerate(libs, 1):
                parts = lib.split("/")
                arch = parts[1] if len(parts) > 2 else "Unknown"
                name = parts[-1]
                table.add_row(str(i), arch, name)

            console.print(table)
            console.print(f"\n[bold cyan]Total Libraries:[/bold cyan] {len(libs)}")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
