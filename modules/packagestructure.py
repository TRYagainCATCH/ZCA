import zipfile
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Package Structure Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    folders = {}

    try:
        with zipfile.ZipFile(apk) as z:
            for f in z.namelist():
                root = f.split("/")[0]
                folders[root] = folders.get(root, 0) + 1

        table = Table(title="Package Structure")
        table.add_column("#", style="yellow")
        table.add_column("Directory", style="green")
        table.add_column("Files", style="cyan")

        for i, (k, v) in enumerate(sorted(folders.items()), 1):
            table.add_row(str(i), k, str(v))

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
