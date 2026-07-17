from rich.prompt import Prompt

from settings import menu
from settings import general
from settings import appearance
from settings import analyzer
from settings import ai
from settings import runtime
from settings import reports
from settings import updates
from settings import backup
from settings import restore
from settings import plugins
from settings import logs
from settings import about


def run():
    while True:
        menu.show()

        choice = Prompt.ask(
            "[bold yellow]Select[/bold yellow]",
            choices=[
                "0","1","2","3","4","5","6",
                "7","8","9","10","11","12"
            ]
        )

        if choice == "1":
            general.run()
        elif choice == "2":
            appearance.run()
        elif choice == "3":
            analyzer.run()
        elif choice == "4":
            ai.run()
        elif choice == "5":
            runtime.run()
        elif choice == "6":
            reports.run()
        elif choice == "7":
            updates.run()
        elif choice == "8":
            backup.run()
        elif choice == "9":
            restore.run()
        elif choice == "10":
            plugins.run()
        elif choice == "11":
            logs.run()
        elif choice == "12":
            about.run()
        elif choice == "0":
            break
