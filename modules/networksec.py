import zipfile
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Network Security Config Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        z = zipfile.ZipFile(apk)

        configs = []

        for f in z.namelist():
            if "network_security" in f.lower():
                configs.append(f)

        table = Table(title="Network Security Files")
        table.add_column("#", style="yellow")
        table.add_column("File", style="green")

        if configs:
            for i, c in enumerate(configs, 1):
                table.add_row(str(i), c)
        else:
            table.add_row("-", "No Network Security Config Found")

        console.print(table)

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
