from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich import box
import time

console = Console()


def clear():
    console.clear()


def logo():
    logo = """
              ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦

                     ███████╗ ██████╗ █████╗
                     ╚══███╔╝██╔════╝██╔══██╗
                       ███╔╝ ██║     ███████║
                      ███╔╝  ██║     ██╔══██║
                     ███████╗╚██████╗██║  ██║
                     ╚══════╝ ╚═════╝╚═╝  ╚═╝

                 ★ Z E D   C O D E   A N A L Y Z E R ★

                 ⚡ Android APK Security Framework ⚡

              ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
"""

    console.print(
        Panel(
            Align.center(
                Text(logo, style="bold bright_cyan")
            ),
            title="[bold bright_green]◈ ZCA v1.0 ◈[/bold bright_green]",
            subtitle="[bold yellow]Developed by Zabiullah[/bold yellow]",
            border_style="bright_magenta",
            box=box.DOUBLE,
            padding=(1, 2),
        )
    )


def header(title):
    console.print()
    console.print(
        Panel.fit(
            f"[bold bright_white]{title}[/bold bright_white]",
            border_style="bright_blue",
            box=box.ROUNDED,
        )
    )


def success(msg):
    console.print(f"[bold green]✔[/bold green] {msg}")


def warning(msg):
    console.print(f"[bold yellow]⚠[/bold yellow] {msg}")


def error(msg):
    console.print(f"[bold red]✘[/bold red] {msg}")


def info(msg):
    console.print(f"[bold cyan]➜[/bold cyan] {msg}")


def loading(text="Initializing ZCA Engine..."):
    with Progress(
        SpinnerColumn(style="bright_cyan"),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(),
        TextColumn("[bold green]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task(text, total=100)
        for _ in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)


def footer():
    console.print(
        Align.center(
            "[bright_black]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bright_black]"
        )
    )
    console.print(
        Align.center(
            "[bold bright_green]ZCA • Android APK Security Framework[/bold bright_green]"
        )
    )
    console.print(
        Align.center(
            "[bright_black]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bright_black]"
        )
    )
