import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

RISK = {
    "CAMERA":"HIGH",
    "RECORD_AUDIO":"HIGH",
    "READ_SMS":"HIGH",
    "SEND_SMS":"HIGH",
    "RECEIVE_SMS":"HIGH",
    "READ_CONTACTS":"HIGH",
    "ACCESS_FINE_LOCATION":"HIGH",
    "ACCESS_COARSE_LOCATION":"MEDIUM",
    "READ_EXTERNAL_STORAGE":"MEDIUM",
    "WRITE_EXTERNAL_STORAGE":"MEDIUM",
    "QUERY_ALL_PACKAGES":"HIGH",
    "SYSTEM_ALERT_WINDOW":"HIGH",
    "MANAGE_EXTERNAL_STORAGE":"HIGH"
}

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Permission Risk Map[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Permission Risk Map")
    table.add_column("#", style="yellow")
    table.add_column("Permission", style="green")
    table.add_column("Risk", style="red")

    n = 1

    try:
        out = subprocess.check_output(
            ["aapt", "dump", "permissions", apk],
            text=True
        )

        for line in out.splitlines():

            if "name='" not in line:
                continue

            perm = line.split("name='")[1].split("'")[0]

            level = "LOW"

            for k, v in RISK.items():
                if k in perm:
                    level = v

            table.add_row(str(n), perm, level)
            n += 1

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
