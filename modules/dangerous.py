import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

DANGEROUS = [
    "READ_SMS",
    "SEND_SMS",
    "RECEIVE_SMS",
    "READ_CONTACTS",
    "WRITE_CONTACTS",
    "READ_CALL_LOG",
    "WRITE_CALL_LOG",
    "PROCESS_OUTGOING_CALLS",
    "RECORD_AUDIO",
    "CAMERA",
    "ACCESS_FINE_LOCATION",
    "ACCESS_COARSE_LOCATION",
    "READ_EXTERNAL_STORAGE",
    "WRITE_EXTERNAL_STORAGE",
    "MANAGE_EXTERNAL_STORAGE",
    "QUERY_ALL_PACKAGES",
    "REQUEST_INSTALL_PACKAGES",
    "SYSTEM_ALERT_WINDOW",
    "PACKAGE_USAGE_STATS"
]

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold red]Dangerous Permissions[/bold red]",
            border_style="red"
        )
    )

    table = Table(title="Dangerous Permissions")
    table.add_column("#", style="yellow")
    table.add_column("Permission", style="red")

    try:
        output = subprocess.check_output(
            ["aapt", "dump", "permissions", apk],
            text=True
        )

        count = 1

        for line in output.splitlines():
            if "name='" not in line:
                continue

            perm = line.split("name='")[1].split("'")[0]

            for d in DANGEROUS:
                if d in perm:
                    table.add_row(str(count), perm)
                    count += 1
                    break

        if count == 1:
            table.add_row("-", "No Dangerous Permissions")

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
