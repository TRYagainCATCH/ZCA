from rich.console import Console

console = Console()

def show():
    console.print("\n[bold cyan]APK Menu[/bold cyan]")
    console.print("[1] APK Information")
    console.print("[2] APK Explorer")
    console.print("[3] Search File")
    console.print("[4] View File")
    console.print("[5] Extract File")
    console.print("[6] Export Report")
    console.print("[0] Back")

    return input("\nSelect Option: ")
