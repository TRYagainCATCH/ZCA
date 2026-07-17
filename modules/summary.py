import subprocess
import zipfile
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]APK Security Summary[/bold green]",
            border_style="green"
        )
    )

    score = 100
    dangerous = 0
    native = 0

    try:
        output = subprocess.check_output(
            ["aapt", "dump", "permissions", apk],
            text=True
        )

        bad = [
            "CAMERA",
            "RECORD_AUDIO",
            "ACCESS_FINE_LOCATION",
            "ACCESS_COARSE_LOCATION",
            "READ_CONTACTS",
            "READ_SMS",
            "SEND_SMS",
            "QUERY_ALL_PACKAGES",
            "MANAGE_EXTERNAL_STORAGE"
        ]

        for line in output.splitlines():
            for p in bad:
                if p in line:
                    dangerous += 1

        score -= dangerous * 3

    except:
        pass

    try:
        with zipfile.ZipFile(apk) as z:
            for f in z.namelist():
                if f.startswith("lib/"):
                    native += 1

        score -= min(native, 10)

    except:
        pass

    if score < 0:
        score = 0

    table = Table(title="Security Summary")
    table.add_column("Item", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Security Score", f"{score}/100")
    table.add_row("Dangerous Permissions", str(dangerous))
    table.add_row("Native Libraries", str(native))

    if score >= 90:
        status = "[green]LOW RISK[/green]"
    elif score >= 70:
        status = "[yellow]MEDIUM RISK[/yellow]"
    else:
        status = "[red]HIGH RISK[/red]"

    table.add_row("Overall", status)

    console.print(table)

    input("\nPress Enter...")
