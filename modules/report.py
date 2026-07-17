import os
import hashlib
import zipfile
from datetime import datetime

from rich.console import Console
from rich.panel import Panel

console = Console()


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            h.update(data)
    return h.hexdigest()


def run(apk):
    console.print(
        Panel.fit(
            "[bold cyan]Report Generator[/bold cyan]",
            border_style="cyan"
        )
    )

    try:
        report_dir = "reports"
        os.makedirs(report_dir, exist_ok=True)

        report_file = os.path.join(
            report_dir,
            os.path.basename(apk) + ".txt"
        )

        with zipfile.ZipFile(apk, "r") as z:
            files = z.namelist()

        with open(report_file, "w", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            f.write("ZCA - ZED CODE ANALYZER REPORT\n")
            f.write("=" * 60 + "\n\n")

            f.write(f"Generated : {datetime.now()}\n")
            f.write(f"APK       : {apk}\n")
            f.write(f"Size      : {round(os.path.getsize(apk)/1024/1024,2)} MB\n")
            f.write(f"SHA256    : {sha256(apk)}\n")
            f.write(f"Files     : {len(files)}\n\n")

            f.write("APK CONTENTS\n")
            f.write("-" * 60 + "\n")

            for item in files:
                f.write(item + "\n")

        console.print(f"\n[bold green]Report saved:[/bold green]")
        console.print(report_file)

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")

    input("\nPress Enter...")
