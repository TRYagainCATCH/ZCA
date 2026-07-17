from rich.prompt import Prompt

from reports import menu
from reports import static_report
from reports import runtime_report
from reports import ai_report
from reports import final_report
from reports import export_pdf
from reports import export_html
from reports import export_json
from reports import history
from reports import settings


def run():
    while True:
        menu.show()

        choice = Prompt.ask(
            "[bold yellow]Select[/bold yellow]",
            choices=["0","1","2","3","4","5","6","7","8","9"]
        )

        if choice == "1":
            static_report.run()
        elif choice == "2":
            runtime_report.run()
        elif choice == "3":
            ai_report.run()
        elif choice == "4":
            final_report.run()
        elif choice == "5":
            export_pdf.run()
        elif choice == "6":
            export_html.run()
        elif choice == "7":
            export_json.run()
        elif choice == "8":
            history.run()
        elif choice == "9":
            settings.run()
        elif choice == "0":
            break
