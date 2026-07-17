from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold red]Universal Bypass Toolkit[/bold red]",
            border_style="red"
        )
    )

    console.print("[bold green]Universal Runtime Bypass[/bold green]\n")

    modules = [
        "Root Detection Bypass",
        "SSL Pinning Bypass",
        "Emulator Detection Bypass",
        "Debugger Detection Bypass",
        "Anti-Frida Bypass",
        "Anti-Tamper Bypass",
        "Anti-VM Detection",
        "Certificate Pinning Bypass",
        "Biometric Bypass",
        "Developer Mode Bypass",
        "Hook Detection Bypass",
        "Custom Script Loader"
    ]

    for i, m in enumerate(modules, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {m}")

    input("\nPress Enter...")
