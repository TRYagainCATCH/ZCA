import zipfile

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

TRACKERS = [
    "facebook",
    "appsflyer",
    "adjust",
    "branch",
    "onesignal",
    "amplitude",
    "mixpanel",
    "firebase",
    "crashlytics",
    "sentry",
    "bugsnag",
    "googleads",
    "admob",
    "google.analytics",
    "analytics",
    "unityads",
    "applovin",
    "ironsource",
    "startapp",
    "chartboost"
]


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]Tracker Detector[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        found = []

        with zipfile.ZipFile(apk, "r") as z:
            for name in z.namelist():

                low = name.lower()

                for tracker in TRACKERS:
                    if tracker in low:
                        found.append(("FILE", tracker))

                try:
                    data = z.read(name).decode("utf-8", errors="ignore").lower()

                    for tracker in TRACKERS:
                        if tracker in data:
                            found.append(("STRING", tracker))

                except:
                    pass

        found = sorted(set(found))

        if not found:
            console.print("[bold red]No trackers detected.[/bold red]")
            input("\nPress Enter...")
            return

        table = Table(title="Detected Trackers")
        table.add_column("#", style="yellow")
        table.add_column("Type", style="cyan")
        table.add_column("Tracker", style="green")

        for i, (t, v) in enumerate(found, 1):
            table.add_row(str(i), t, v)

        console.print(table)
        console.print(f"\n[bold cyan]Total Trackers:[/bold cyan] {len(found)}")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
