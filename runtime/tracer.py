from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold magenta]Method Tracer[/bold magenta]",
            border_style="magenta"
        )
    )

    console.print("[bold green]Runtime Method Tracing[/bold green]\n")

    methods = [
        "Java Method Hooks",
        "Native Function Hooks",
        "JNI Method Tracing",
        "Class Loader Trace",
        "Reflection Monitor",
        "Constructor Trace",
        "Thread Trace",
        "Stack Trace",
        "Call Graph",
        "Arguments Logger",
        "Return Value Logger",
        "Export Trace Report"
    ]

    for i, method in enumerate(methods, 1):
        console.print(f"[cyan]{i:02}[/cyan]  {method}")

    input("\nPress Enter...")
