import zipfile
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

KEYWORDS = {
    "AES":"AES Encryption",
    "DES":"DES Encryption",
    "RSA":"RSA Encryption",
    "EC":"Elliptic Curve",
    "SHA-1":"SHA-1",
    "SHA-256":"SHA-256",
    "SHA-512":"SHA-512",
    "MD5":"MD5",
    "Cipher":"Cipher API",
    "SecretKey":"Secret Key",
    "KeyGenerator":"Key Generator",
    "KeyStore":"Android KeyStore",
    "MessageDigest":"Message Digest",
    "Mac":"HMAC",
    "Signature":"Digital Signature",
    "SecureRandom":"Secure Random"
}

def run(apk):
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Crypto Analyzer[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(title="Cryptography Usage")
    table.add_column("#", style="yellow")
    table.add_column("Algorithm", style="green")
    table.add_column("Description", style="cyan")

    count = 1

    try:
        with zipfile.ZipFile(apk) as z:
            for f in z.namelist():
                try:
                    data = z.read(f).decode(errors="ignore")
                    for k, v in KEYWORDS.items():
                        if k in data:
                            table.add_row(str(count), k, v)
                            count += 1
                except:
                    pass

        if count == 1:
            table.add_row("-", "No Crypto APIs Found", "-")

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

    input("\nPress Enter...")
