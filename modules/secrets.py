import re
import zipfile

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

PATTERNS = {
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "GitHub Token": r"ghp_[A-Za-z0-9]{36}",
    "Bearer Token": r"Bearer\s+[A-Za-z0-9\-._~+/]+=*",
    "JWT": r"eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+",
    "Private Key": r"-----BEGIN PRIVATE KEY-----",
    "Password": r"password\s*[:=]\s*['\"]?.+",
    "Secret": r"secret\s*[:=]\s*['\"]?.+",
    "API Key": r"api[_-]?key\s*[:=]\s*['\"]?.+",
}


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]Hardcoded Secrets Scanner[/bold cyan]",
            border_style="cyan"
        )
    )

    results = []

    try:
        with zipfile.ZipFile(apk, "r") as z:
            for name in z.namelist():
                try:
                    data = z.read(name).decode("utf-8", errors="ignore")

                    for title, pattern in PATTERNS.items():
                        for m in re.findall(pattern, data):
                            results.append((title, m[:80]))

                except:
                    pass

        if not results:
            console.print("[bold red]No secrets found.[/bold red]")
            input("\nPress Enter...")
            return

        table = Table(title="Detected Secrets")
        table.add_column("#", style="yellow")
        table.add_column("Type", style="cyan")
        table.add_column("Value", style="green")

        seen = set()

        i = 1
        for t, v in results:
            if (t, v) not in seen:
                seen.add((t, v))
                table.add_row(str(i), t, v)
                i += 1

        console.print(table)
        console.print(f"\n[bold cyan]Total Findings:[/bold cyan] {len(seen)}")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
