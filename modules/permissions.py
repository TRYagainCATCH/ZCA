import subprocess
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

DANGEROUS = [
    "READ_SMS",
    "SEND_SMS",
    "RECEIVE_SMS",
    "READ_CONTACTS",
    "WRITE_CONTACTS",
    "READ_CALL_LOG",
    "WRITE_CALL_LOG",
    "RECORD_AUDIO",
    "CAMERA",
    "ACCESS_FINE_LOCATION",
    "ACCESS_COARSE_LOCATION",
    "READ_EXTERNAL_STORAGE",
    "WRITE_EXTERNAL_STORAGE",
    "READ_MEDIA_IMAGES",
    "READ_MEDIA_VIDEO",
    "QUERY_ALL_PACKAGES",
    "REQUEST_INSTALL_PACKAGES",
    "SYSTEM_ALERT_WINDOW",
    "PACKAGE_USAGE_STATS",
    "MANAGE_EXTERNAL_STORAGE",
]

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Permissions Risk Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        output = subprocess.check_output(
            ["aapt", "dump", "permissions", apk],
            text=True
        )

        table = Table(title="Permissions")
        table.add_column("#", style="yellow")
        table.add_column("Permission", style="green")
        table.add_column("Risk", style="red")

        count = 1

        for line in output.splitlines():

            if not line.startswith("uses-permission"):
                continue

            if "name='" not in line:
                continue

            perm = line.split("name='")[1].split("'")[0]

            risk = "[green]LOW[/green]"

            for p in DANGEROUS:
                if p in perm:
                    risk = "[bold red]DANGEROUS[/bold red]"
                    break

            table.add_row(str(count), perm, risk)
            count += 1

        console.print(table)
        console.print(f"\n[bold cyan]Total Permissions:[/bold cyan] {count-1}")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
