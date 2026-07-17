import zipfile
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Interesting Strings Finder[/bold cyan]",
            border_style="cyan"
        )
    )

    KEYWORDS = [
        "token",
        "apikey",
        "api_key",
        "secret",
        "password",
        "passwd",
        "firebase",
        "bearer",
        "authorization",
        "oauth",
        "jwt",
        "private",
        "client_secret",
        "access_key",
        "username",
        "email"
    ]

    table = Table(title="Interesting Strings")
    table.add_column("#", style="yellow")
    table.add_column("Keyword", style="cyan")
    table.add_column("Match", style="green")

    count = 1

    try:
        with zipfile.ZipFile(apk) as z:
            for f in z.namelist():
                try:
                    data = z.read(f).decode(errors="ignore")
                    low = data.lower()

                    for k in KEYWORDS:
                        if k in low:
                            table.add_row(
                                str(count),
                                k,
                                f[:80]
                            )
                            count += 1
                except:
                    pass

        if count == 1:
            table.add_row("-", "Nothing Found", "-")

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
