import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def get_value(text, key):
    for line in text.splitlines():
        if line.startswith(key):
            return line.replace(key, "").replace("'", "")
    return "-"

def run(apk):
    console.print(
        Panel.fit(
            "[bold green]AAPT Summary[/bold green]",
            border_style="green"
        )
    )

    result = subprocess.run(
        ["aapt", "dump", "badging", apk],
        capture_output=True,
        text=True
    )

    out = result.stdout

    table = Table(title="APK Summary")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Package", get_value(out, "package: name="))
    table.add_row("Version", get_value(out, "versionName="))
    table.add_row("Min SDK", get_value(out, "sdkVersion:"))
    table.add_row("Target SDK", get_value(out, "targetSdkVersion:"))
    table.add_row("App Name", get_value(out, "application-label:"))
    table.add_row("Main Activity", get_value(out, "launchable-activity: name="))
    table.add_row("Architecture", get_value(out, "native-code:"))

    console.print(table)

    console.print("\n[bold yellow]Permissions[/bold yellow]")

    for line in out.splitlines():
        if line.startswith("uses-permission:"):
            console.print("[green]•[/green] " + line.replace("uses-permission: name=", "").replace("'", ""))

    input("\nPress Enter...")
