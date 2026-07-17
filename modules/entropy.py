import math
import zipfile
from collections import Counter
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def entropy(data):
    if not data:
        return 0
    c = Counter(data)
    l = len(data)
    return -sum((x/l) * math.log2(x/l) for x in c.values())

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]File Entropy Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Top Entropy Files")
    table.add_column("#", style="yellow")
    table.add_column("File", style="green")
    table.add_column("Entropy", style="red")

    try:
        files = []

        with zipfile.ZipFile(apk) as z:
            for f in z.namelist():
                try:
                    e = entropy(z.read(f))
                    files.append((f, e))
                except:
                    pass

        files.sort(key=lambda x: x[1], reverse=True)

        for i, (f, e) in enumerate(files[:50], 1):
            table.add_row(str(i), f, f"{e:.2f}")

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
