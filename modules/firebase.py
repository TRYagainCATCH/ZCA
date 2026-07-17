import zipfile

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


KEYWORDS = [
    "firebase",
    "google-services.json",
    "google_app_id",
    "gcm_defaultSenderId",
    "google_api_key",
    "google_crashlytics",
    "crashlytics",
    "analytics",
    "remoteconfig",
    "remote_config",
    "firebasemessaging",
    "messaging",
    "fcm",
]


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]Firebase Detector[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        found = []

        with zipfile.ZipFile(apk, "r") as z:
            for name in z.namelist():

                low = name.lower()

                for key in KEYWORDS:
                    if key in low:
                        found.append(("FILE", name))
                        break

                try:
                    data = z.read(name).decode("utf-8", errors="ignore").lower()

                    for key in KEYWORDS:
                        if key in data:
                            found.append(("STRING", key))
                except:
                    pass

        if not found:
            console.print("[bold red]Firebase not detected.[/bold red]")
            input("\nPress Enter...")
            return

        table = Table(title="Firebase Results")
        table.add_column("#", style="yellow")
        table.add_column("Type", style="cyan")
        table.add_column("Value", style="green")

        seen = set()

        i = 1
        for t, v in found:
            if (t, v) not in seen:
                seen.add((t, v))
                table.add_row(str(i), t, v)
                i += 1

        console.print(table)
        console.print(f"\n[bold cyan]Total Findings:[/bold cyan] {len(seen)}")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
