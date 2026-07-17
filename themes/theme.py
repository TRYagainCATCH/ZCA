from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

console = Console()

# ===== COLORS =====
PRIMARY = "bright_cyan"
SECONDARY = "bright_green"
WARNING = "yellow"
ERROR = "bright_red"
INFO = "bright_blue"
TITLE = "bright_magenta"

LINE = "[bright_black]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bright_black]"


def line():
    console.print(LINE)


def logo():
    banner = Text("""
★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★

              ███████╗ ██████╗ █████╗
              ╚══███╔╝██╔════╝██╔══██╗
                ███╔╝ ██║     ███████║
               ███╔╝  ██║     ██╔══██║
              ███████╗╚██████╗██║  ██║
              ╚══════╝ ╚═════╝╚═╝  ╚═╝

          ★ Z E D   C O D E   A N A L Y Z E R ★

        Android APK Reverse Engineering Framework

★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★
""", style=PRIMARY)

    console.print(
        Panel(
            Align.center(banner),
            title="[bold bright_green]◈ ZCA Framework ◈[/bold bright_green]",
            subtitle="[bold yellow]Android Security Toolkit[/bold yellow]",
            border_style="bright_magenta",
            box=box.DOUBLE,
            padding=(1, 2),
        )
    )


def title(name):
    console.print(
        Panel.fit(
            f"[bold white]{name}[/bold white]",
            border_style="bright_blue",
            box=box.ROUNDED,
        )
    )


def success(msg):
    console.print(f"[bold bright_green][✔][/bold bright_green] {msg}")


def error(msg):
    console.print(f"[bold bright_red][✘][/bold bright_red] {msg}")


def warning(msg):
    console.print(f"[bold yellow][!][/bold yellow] {msg}")


def info(msg):
    console.print(f"[bold bright_cyan][➜][/bold bright_cyan] {msg}")


def footer():
    console.print(LINE)
    console.print(
        Align.center(
            "[bold bright_green]ZCA • Android APK Analysis Framework[/bold bright_green]"
        )
    )
    console.print(LINE)
