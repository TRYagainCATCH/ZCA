import zipfile
from rich.console import Console

console = Console()

def run(apk):
    name = input("File Name: ").strip()

    try:
        with zipfile.ZipFile(apk, "r") as z:
            data = z.read(name)

            try:
                text = data.decode("utf-8", errors="ignore")
                console.print(text[:5000])
            except:
                console.print("[red]Binary file. Cannot display.[/red]")

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
