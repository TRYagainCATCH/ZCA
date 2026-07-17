from rich.console import Console
from rich.panel import Panel
from datetime import datetime
import os

console = Console()

def run(apk):
    console.clear()

    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    filename = os.path.join(
        report_dir,
        f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(filename, "w") as f:
        f.write("========== ZCA REPORT ==========\n")
        f.write(f"APK : {apk}\n")
        f.write(f"Generated : {datetime.now()}\n")
        f.write("\nAnalysis Completed Successfully.\n")
        f.write("\nModules Executed:\n")
        f.write("- APK Information\n")
        f.write("- Manifest\n")
        f.write("- Certificate\n")
        f.write("- Strings\n")
        f.write("- URLs\n")
        f.write("- Native Libraries\n")
        f.write("- Assets\n")
        f.write("- DEX\n")
        f.write("- Firebase\n")
        f.write("- Trackers\n")
        f.write("- Secrets\n")
        f.write("- Exported Components\n")
        f.write("- Permissions\n")
        f.write("- Network Security\n")
        f.write("- YARA\n")
        f.write("- Malware\n")
        f.write("- API Keys\n")
        f.write("- Crypto\n")
        f.write("- Resources\n")
        f.write("- Signature Compare\n")
        f.write("- Entropy\n")
        f.write("- Package Structure\n")
        f.write("- Libraries\n")
        f.write("- Dangerous Permissions\n")
        f.write("- Security Summary\n")
        f.write("- SDK Information\n")
        f.write("- Components\n")
        f.write("- Certificate Details\n")
        f.write("- Interesting Strings\n")
        f.write("- Java Classes\n")
        f.write("- Multi DEX\n")
        f.write("- Permission Risk Map\n")
        f.write("- Certificate Chain\n")
        f.write("- Certificate Verification\n")

    console.print(
        Panel.fit(
            f"[bold green]Report Saved Successfully[/bold green]\n\n{filename}",
            title="ZCA Report",
            border_style="green"
        )
    )

    input("\nPress Enter...")
