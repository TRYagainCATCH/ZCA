import re
import zipfile
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

PATTERNS = {
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Firebase URL": r"https://[A-Za-z0-9\-]+\.firebaseio\.com",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Stripe Live Key": r"sk_live_[0-9A-Za-z]+",
    "Stripe Test Key": r"sk_test_[0-9A-Za-z]+",
    "GitHub Token": r"ghp_[A-Za-z0-9]{36}",
    "OpenAI Key": r"sk-[A-Za-z0-9]{20,}"
}

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]API Key Detector[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Detected Keys")
    table.add_column("#", style="yellow")
    table.add_column("Type", style="cyan")
    table.add_column("Value", style="green")

    count = 1

    try:
        with zipfile.ZipFile(apk) as z:
            for f in z.namelist():
                try:
                    data = z.read(f).decode(errors="ignore")

                    for name, pattern in PATTERNS.items():
                        for m in re.findall(pattern, data):
                            table.add_row(str(count), name, m[:60])
                            count += 1

                except:
                    pass

        if count == 1:
            table.add_row("-", "No API Keys Found", "-")

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
