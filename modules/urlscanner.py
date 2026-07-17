import os
import re
import zipfile
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

URL_RE = r"https?://[^\s\"'<>]+"
EMAIL_RE = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
IP_RE = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"


def run(apk):
    os.system("clear")

    console.print(
        Panel.fit(
            "[bold cyan]URL & Endpoint Scanner[/bold cyan]",
            border_style="cyan"
        )
    )

    found = set()

    try:
        with zipfile.ZipFile(apk, "r") as z:
            for name in z.namelist():
                try:
                    text = z.read(name).decode("utf-8", errors="ignore")

                    for x in re.findall(URL_RE, text):
                        found.add(("URL", x))

                    for x in re.findall(EMAIL_RE, text):
                        found.add(("EMAIL", x))

                    for x in re.findall(IP_RE, text):
                        found.add(("IP", x))

                except:
                    pass

        table = Table(title="Endpoints")
        table.add_column("#", style="cyan")
        table.add_column("Type", style="yellow")
        table.add_column("Value", style="green")

        for i, (t, v) in enumerate(sorted(found)[:100], 1):
            table.add_row(str(i), t, v)

        console.print(table)
        console.print(f"\n[bold green]Total:[/bold green] {len(found)}")

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
