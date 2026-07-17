from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import zipfile

console = Console()

RULES = {
    "bank": "Banking",
    "root": "Root Detection",
    "frida": "Frida",
    "xposed": "Xposed",
    "magisk": "Magisk",
    "su": "Root Binary",
    "dexclassloader": "Dynamic Code Loading",
    "runtime.exec": "Command Execution",
    "base64": "Encoded Data"
}

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]YARA Style Scanner[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Matched Rules")
    table.add_column("#", style="yellow")
    table.add_column("Keyword", style="green")
    table.add_column("Description", style="cyan")

    count = 1

    try:
        with zipfile.ZipFile(apk) as z:
            for f in z.namelist():
                try:
                    data = z.read(f).decode(errors="ignore").lower()
                    for key, desc in RULES.items():
                        if key in data:
                            table.add_row(str(count), key, desc)
                            count += 1
                except:
                    pass

        if count == 1:
            table.add_row("-", "No Match", "-")

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
