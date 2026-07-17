import os
import re
import zipfile
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(apk):
    os.system("clear")

    console.print(
        Panel.fit(
            "[bold green]Strings Analyzer[/bold green]",
            border_style="green"
        )
    )

    strings = set()

    try:
        with zipfile.ZipFile(apk, "r") as z:
            for name in z.namelist():
                try:
                    data = z.read(name)
                    text = data.decode("utf-8", errors="ignore")
                    for s in re.findall(r"[ -~]{8,}", text):
                        strings.add(s)
                except:
                    pass

        table = Table(title="Strings")
        table.add_column("#", style="cyan")
        table.add_column("String", style="green")

        for i, s in enumerate(sorted(strings)[:100], 1):
            table.add_row(str(i), s)

        console.print(table)
        console.print(f"\n[bold cyan]Total Strings:[/bold cyan] {len(strings)}")

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
