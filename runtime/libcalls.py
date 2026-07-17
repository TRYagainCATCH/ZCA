from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Native Library Calls[/bold cyan]",
            border_style="cyan"
        )
    )

    console.print("[bold green]Native Runtime Analysis[/bold green]\n")

    calls = [
        "libc.so",
        "libart.so",
        "libandroid.so",
        "liblog.so",
        "libssl.so",
        "libcrypto.so",
        "libsqlite.so",
        "libc++_shared.so",
        "libOpenSLES.so",
        "libEGL.so",
        "libGLESv2.so",
        "JNI Native Methods",
        "dlopen() Calls",
        "dlsym() Calls",
        "System Calls",
        "Memory Functions",
        "File Functions",
        "Network Functions",
        "Crypto Functions",
        "Export Analysis Report"
    ]

    for i, call in enumerate(calls, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {call}")

    input("\nPress Enter...")
