import zipfile
from rich.console import Console

console = Console()

def run(apk):
    word = input("Search: ").strip().lower()

    with zipfile.ZipFile(apk, "r") as z:
        found = False
        for f in z.namelist():
            if word in f.lower():
                console.print(f"[green]{f}[/green]")
                found = True

        if not found:
            console.print("[red]No matching file found.[/red]")

    input("\nPress Enter...")
