from rich.prompt import Prompt

from ai import menu
from ai import malware_ai
from ai import code_explainer
from ai import vuln_predictor
from ai import permission_ai
from ai import api_ai
from ai import string_ai
from ai import url_ai
from ai import behavior_ai
from ai import yara_ai
from ai import risk_score
from ai import summary_ai
from ai import report_ai
from ai import recommendations
from ai import model_info
from ai import settings


def run():
    while True:
        menu.show()

        choice = Prompt.ask(
            "[bold yellow]Select[/bold yellow]",
            choices=[
                "0","1","2","3","4","5","6","7",
                "8","9","10","11","12","13","14","15"
            ]
        )

        if choice == "1":
            malware_ai.run()
        elif choice == "2":
            code_explainer.run()
        elif choice == "3":
            vuln_predictor.run()
        elif choice == "4":
            permission_ai.run()
        elif choice == "5":
            api_ai.run()
        elif choice == "6":
            string_ai.run()
        elif choice == "7":
            url_ai.run()
        elif choice == "8":
            behavior_ai.run()
        elif choice == "9":
            yara_ai.run()
        elif choice == "10":
            risk_score.run()
        elif choice == "11":
            summary_ai.run()
        elif choice == "12":
            report_ai.run()
        elif choice == "13":
            recommendations.run()
        elif choice == "14":
            model_info.run()
        elif choice == "15":
            settings.run()
        elif choice == "0":
            break

