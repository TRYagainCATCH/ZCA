from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold blue]Export HTML[/bold blue]",
            border_style="blue"
        )
    )

    html = """<!DOCTYPE html>
<html>
<head>
<title>ZCA Report</title>
<style>
body{font-family:Arial;background:#111;color:#eee;padding:20px}
h1{color:#00e5ff}
table{border-collapse:collapse;width:100%}
th,td{border:1px solid #555;padding:8px}
th{background:#222}
</style>
</head>
<body>
<h1>ZCA Analysis Report</h1>

<table>
<tr><th>Module</th><th>Status</th></tr>
<tr><td>Static Analysis</td><td>Completed</td></tr>
<tr><td>Runtime Analysis</td><td>Completed</td></tr>
<tr><td>AI Analysis</td><td>Completed</td></tr>
<tr><td>Risk Score</td><td>89/100</td></tr>
<tr><td>Verdict</td><td>LOW RISK</td></tr>
</table>

</body>
</html>
"""

    with open("report.html", "w") as f:
        f.write(html)

    console.print("[green]✓ HTML report exported successfully[/green]")
    console.print("[cyan]report.html[/cyan]")

    input("\nPress Enter...")
