import zipfile
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

LIBRARIES = [
    "firebase",
    "okhttp",
    "retrofit",
    "glide",
    "coil",
    "picasso",
    "gson",
    "moshi",
    "room",
    "workmanager",
    "androidx",
    "kotlin",
    "compose",
    "stripe",
    "facebook",
    "adjust",
    "branch",
    "play-services",
    "mlkit",
    "opencv"
]

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Library Detector[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Detected Libraries")
    table.add_column("#", style="yellow")
    table.add_column("Library", style="green")
    table.add_column("Status", style="cyan")

    count = 1

    try:
        with zipfile.ZipFile(apk) as z:
            files = "\n".join(z.namelist()).lower()

            for lib in LIBRARIES:
                if lib in files:
                    table.add_row(str(count), lib, "Detected")
                    count += 1

        if count == 1:
            table.add_row("-", "No Known Libraries", "-")

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
