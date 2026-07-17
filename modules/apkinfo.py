from modules import finalreport
from modules import certificateverify
from modules import certificatechain
from modules import permissionsmap
from modules import multidex
from modules import classes
from modules import stringssearch
from modules import certdetails
from modules import components
from modules import sdkinfo
from modules import summary
from modules import dangerous
from modules import libraries
from modules import packagestructure
from modules import entropy
from modules import signaturecompare
from modules import resources
from modules import crypto
from modules import apikeys
from modules import malware
from modules import yara
from modules import deepmanifest
from modules import networksec
from modules import permissions
import os
import zipfile
import hashlib
import magic
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from modules import obfuscation
from modules import report
from modules import exported
from modules import secrets
from modules import tracker
from modules import firebase
from modules import dex
from modules import assets
from modules import nativelibs
from modules import urlscanner
from modules import search
from modules import viewfile
from modules import aaptinfo
from modules import manifest
from modules import certificate
from modules import strings

console = Console()


def get_hash(path, algo):
    h = algo()
    with open(path, "rb") as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            h.update(data)
    return h.hexdigest()


def run():
    os.system("clear")

    console.print(
        Panel.fit(
            "[bold cyan]ZCA APK Information Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    apk = input("Enter APK Path: ").strip()

    if not os.path.isfile(apk):
        console.print("[bold red]File not found![/bold red]")
        input("Press Enter...")
        return

    info = Table(title="APK Basic Information")
    info.add_column("Field", style="cyan")
    info.add_column("Value", style="green")

    info.add_row("File Name", os.path.basename(apk))
    info.add_row("Absolute Path", os.path.abspath(apk))
    info.add_row("Size", f"{round(os.path.getsize(apk)/1024/1024,2)} MB")
    info.add_row("Type", magic.from_file(apk))
    info.add_row("MD5", get_hash(apk, hashlib.md5))
    info.add_row("SHA1", get_hash(apk, hashlib.sha1))
    info.add_row("SHA256", get_hash(apk, hashlib.sha256))

    console.print(info)

    try:
        with zipfile.ZipFile(apk, "r") as z:
            files = z.namelist()

            table = Table(title="APK Contents")
            table.add_column("#", style="yellow")
            table.add_column("File", style="green")

            for i, f in enumerate(files[:30], 1):
                table.add_row(str(i), f)

            console.print(table)
            console.print(f"[bold cyan]Total Files:[/bold cyan] {len(files)}")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")
        input("Press Enter...")
        return

    while True:
        console.print("\n[bold yellow]APK Menu[/bold yellow]")
        console.print("[1] Search File")
        console.print("[2] View File")
        console.print("[3] AAPT Summary")
        console.print("[4] AndroidManifest Analyzer")
        console.print("[5] Certificate Analyzer")
        console.print("[6] Strings Analyzer")
        console.print("[7] URL & Endpoint Scanner")
        console.print("[8] Native Libraries")
        console.print("[9] Assets Analyzer")
        console.print("[10] DEX Analyzer")
        console.print("[11] Firebase Detector")
        console.print("[12] Tracker Detector")
        console.print("[13] Hardcoded Secrets")
        console.print("[14] Exported Components")
        console.print("[15] Generate Report")
        console.print("[16] Code Obfuscation Detector")
        console.print("[17] Permissions Risk Analyzer")
        console.print("[18] Network Security Config")
        console.print("[19] Deep Manifest Viewer")
        console.print("[20] YARA Scanner")
        console.print("[21] Malware Heuristics")
        console.print("[22] API Key Detector")
        console.print("[23] Crypto Analyzer")
        console.print("[24] Resources Analyzer")
        console.print("[25] APK Signature Compare")
        console.print("[26] File Entropy Analyzer")
        console.print("[27] Package Structure")
        console.print("[28] Library Detector")
        console.print("[29] Dangerous Permissions")
        console.print("[30] APK Security Summary")
        console.print("[31] SDK Information")
        console.print("[32] Application Components")
        console.print("[33] Certificate Details")
        console.print("[34] Interesting Strings Finder")
        console.print("[35] Java Classes Analyzer")
        console.print("[36] Multi DEX Analyzer")
        console.print("[37] Permission Risk Map")
        console.print("[38] Certificate Chain Analyzer")
        console.print("[39] Certificate Verification")
        console.print("[40] Final Analysis Report")
        console.print("[0] Back")

        choice = input("Select: ")

        if choice == "1":
            search.run(apk)

        elif choice == "2":
            viewfile.run(apk)

        elif choice == "3":
            aaptinfo.run(apk)

        elif choice == "4":
            manifest.run(apk)

        elif choice == "5":
            certificate.run(apk)

        elif choice == "6":
            strings.run(apk)

        elif choice == "7":
            urlscanner.run(apk) 

        elif choice == "8":
            nativelibs.run(apk) 

        elif choice == "9":
            assets.run(apk)

        elif choice == "10":
            dex.run(apk)
   
        elif choice == "11":
            firebase.run(apk)

        elif choice == "12":
            tracker.run(apk)

        elif choice == "13":
            secrets.run(apk)

        elif choice == "14":
            exported.run(apk)

        elif choice == "15":
            report.run(apk)

        elif choice == "16":
            obfuscation.run(apk)

        elif choice == "17":
            permissions.run(apk)

        elif choice == "18":
            networksec.run(apk)

        elif choice == "19":
            deepmanifest.run(apk)

        elif choice == "20":
            yara.run(apk)

        elif choice == "21":
            malware.run(apk)

        elif choice == "22":
            apikeys.run(apk)

        elif choice == "23":
            crypto.run(apk)

        elif choice == "24":
            resources.run(apk)

        elif choice == "25":
            signaturecompare.run(apk)

        elif choice == "26":
            entropy.run(apk)

        elif choice == "27":
            packagestructure.run(apk)

        elif choice == "28":
            libraries.run(apk)

        elif choice == "29":
            dangerous.run(apk)

        elif choice == "30":
            summary.run(apk)

        elif choice == "31":
            sdkinfo.run(apk)

        elif choice == "32":
            components.run(apk)

        elif choice == "33":
            certdetails.run(apk)

        elif choice == "34":
            stringssearch.run(apk)

        elif choice == "35":
            classes.run(apk)

        elif choice == "36":
            multidex.run(apk)

        elif choice == "37":
            permissionsmap.run(apk)

        elif choice == "38":
            certificatechain.run(apk)

        elif choice == "39":
            certificateverify.run(apk)

        elif choice == "40":
            finalreport.run(apk)

        elif choice == "0":
            break

        else:
            console.print("[bold red]Invalid Option[/bold red]")
