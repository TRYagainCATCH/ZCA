import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]AndroidManifest Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        result = subprocess.run(
            ["aapt", "dump", "xmltree", apk, "AndroidManifest.xml"],
            capture_output=True,
            text=True
        )

        output = result.stdout.splitlines()

        permissions = []
        activities = []
        services = []
        receivers = []
        providers = []

        for line in output:
            line = line.strip()

            if "uses-permission" in line:
                permissions.append(line)

            elif "E: activity" in line:
                activities.append(line)

            elif "E: service" in line:
                services.append(line)

            elif "E: receiver" in line:
                receivers.append(line)

            elif "E: provider" in line:
                providers.append(line)

        def show(title, data):
            table = Table(title=title)
            table.add_column("#", style="yellow")
            table.add_column("Value", style="green")

            if not data:
                table.add_row("-", "None")

            else:
                for i, item in enumerate(data, 1):
                    table.add_row(str(i), item)

            console.print(table)

        show("Permissions", permissions)
        show("Activities", activities)
        show("Services", services)
        show("Receivers", receivers)
        show("Providers", providers)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
