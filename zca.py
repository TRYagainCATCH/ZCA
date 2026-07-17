#!/usr/bin/env python3

from settings import settings
from reports import reports
from ai import ai
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
from rich import box

from themes import theme
from modules import static
from runtime import runtime
console = Console()


def clear():
    os.system("clear")


def banner():
    theme.logo()


def menu():
    menu_text = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🛡  [1] Static Analyzer
⚡  [2] Runtime Analyzer
🤖  [3] AI Analyzer
📄  [4] Reports
⚙  [5] Settings

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌  [0] Exit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    console.print(
        Panel(
            Align.center(menu_text),
            title="[bold bright_green]MAIN MENU[/bold bright_green]",
            subtitle="[bold cyan]ZCA Framework[/bold cyan]",
            border_style="bright_blue",
            box=box.DOUBLE,
        )
    )


while True:
    clear()

    banner()
    theme.line()
    menu()

    choice = Prompt.ask(
        "[bold yellow]Select Option[/bold yellow]",
        choices=["0", "1", "2", "3", "4", "5"]
    )

    if choice == "1":
        static.run()

    elif choice == "2":
        runtime.run()
 
    elif choice == "3":
        ai.run()

    elif choice == "4":
        reports.run() 
 
    elif choice == "5":
        settings.run() 

    elif choice == "0":
        console.print(
            Panel.fit(
                "[bold red]Thanks for using ZCA![/bold red]",
                border_style="red",
            )
        )
        break
