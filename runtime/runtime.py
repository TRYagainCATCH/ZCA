from rich.prompt import Prompt
from runtime import menu
from runtime import frida
from runtime import memory
from runtime import sslpinning
from runtime import rootdetect
from runtime import antiemulator
from runtime import api_monitor
from runtime import filesystem
from runtime import network
from runtime import process
from runtime import javascript
from runtime import dumpdex
from runtime import bypass
from runtime import tracer
from runtime import logcat
from runtime import libcalls
from runtime import report

def run():
    while True:
        menu.show()

        choice = Prompt.ask(
            "[bold yellow]Select[/bold yellow]",
            choices=[
                "0","1","2","3","4","5","6","7",
                "8","9","10","11","12","13","14","15","16"
            ]
        )

        if choice == "1":
            frida.run()
        elif choice == "2":
            memory.run()
        elif choice == "3":
            sslpinning.run()
        elif choice == "4":
            rootdetect.run()
        elif choice == "5":
            antiemulator.run()
        elif choice == "6":
            api_monitor.run()
        elif choice == "7":
            filesystem.run()
        elif choice == "8":
            network.run()
        elif choice == "9":
            process.run()
        elif choice == "10":
            javascript.run()
        elif choice == "11":
            dumpdex.run()
        elif choice == "12":
            bypass.run()
        elif choice == "13":
            tracer.run()
        elif choice == "14":
            logcat.run()
        elif choice == "15":
            libcalls.run()
        elif choice == "16":
            report.run()
        elif choice == "0":
            break
