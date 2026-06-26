import subprocess
import sys
import os
import colorama
from colorama import init, Fore


init ()

print(Fore.RED, end="")
# ─────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────


APPS = {
    "1": {
        "name": "Discord",
        "win":  r"C:\Users\%USERNAME%\AppData\Local\Discord\Update.exe --processStart Discord.exe",
        "linux": "discord",
        "mac":  "open -a Discord",
    },
    "2": {
        "name": "Riot Client",
        "win":  r"C:\Riot Games\Riot Client\RiotClientServices.exe",
        "linux": "riot-client",
        "mac":  "open -a 'Riot Client'",
    },
    "3": {
        "name": "Epic Games",
        "win":  r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe",
        "linux": "heroic",          # alternative Linux
        "mac":  "open -a 'Epic Games Launcher'",
    },
    "4": {
        "name": "Steam",
        "win":  r"C:\Program Files (x86)\Steam\steam.exe",
        "linux": "steam",
        "mac":  "open -a Steam",
    },
    "5": {
        "name": "Brave",
        "win":  r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "linux": "brave-browser",
        "mac":  "open -a 'Brave Browser'",
    },
    "6": {
        "name": "Dossier Tout (Bureau)",
        "win":  r"explorer %USERPROFILE%\Desktop\tout",
    },
    "10": {
        "name": "Visual Studio Code",
        "win":  r"code",
        "linux": "code",
        "mac":  "open -a 'Visual Studio Code'",
    },
    "7": {
        "name": "Proton VPN",
        "win":  r"C:\Program Files\Proton\VPN\ProtonVPN.exe",
        "linux": "protonvpn-app",
        "mac":  "open -a 'Proton VPN'",
    },
    "8": {
        "name": "Spotify",
        "win":  r"C:\%USERPROFILE%\AppData\Roaming\Spotify\Spotify.exe",
    },
    "11": {
        "name": "Token",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Get-Token.py",
    },
    "14": {
        "name": "Ip Look Up",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Ip-LookUp.py",
    },
    "12": {
        "name": "Discord Invite Info",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Discord_Invite_Info.py",
    },
    "13": {
        "name": "Discord ID Info",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Discord_Id_Info.py",
    },
    "15": {
        "name": "Discord Nuke Add and Suppr",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Add and Suppr.exe",
    },
    "16": {
        "name": "Discord Nuke Add and Suppr random name",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Add and Suppr random name.exe",
    },
    "17": {
        "name": "Only Suppr",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Only Suppr.exe",
    },
    "18": {
        "name": "Url Info",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Url_Info.py",
    },
    "19": {
        "name": "Roblox ID info",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Roblox_Id_Info.py",
    },
    "20": {
        "name": "Roblox User info",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Roblox_User_Info.py",
    },
    "21": {
        "name": "Tiktok ID Look Up",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Tiktok_Id_Info.py",
    },
    "22": {
        "name": "Tiktok User Look Up",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Tiktok_User_Info.py",
    },
    "23": {
        "name": "Instagram Look Up",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Instagram_Lookup.py",
    },
    "24": {
        "name": "WebHook Spammer",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Discord_Webhook_Sender.py",
    },
    "25": {
        "name": "WebHook Spammer",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\macro200.exe",
    },
    "26": {
        "name": "Movement Apex Config",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Config_Apex.exe",
    },
    "27": {
        "name": "Webhook Message",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Discord_Webhook_Chat.py",
    },
    "28": {
        "name": "Token Tester",
        "win":  r"explorer %USERPROFILE%\Desktop\Tool\Config\Token_Tester.py",
    },
}
    

BRAVE_SITES = {
    "1": ("YouTube",  "https://www.youtube.com"),
    "2": ("Twitch",   "https://www.twitch.tv"),
    "3": ("Netflix",  "https://www.netflix.com"),
}

BRAVE_CMD = {
    "win":   r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    "linux": "brave-browser",
    "mac":   "open -a 'Brave Browser'",
}

# ─────────────────────────────────────────────
#  WIN LINUX OU MAC ( TRUC DES RICHES ON SAIT JAMAIS WLH )
# ─────────────────────────────────────────────

def get_platform():
    if sys.platform.startswith("win"):
        return "win"
    elif sys.platform.startswith("darwin"):
        return "mac"
    else:
        return "linux"

PLATFORM = get_platform()

# ─────────────────────────────────────────────
#  LANCE
# ─────────────────────────────────────────────

def launch(cmd: str):
    """Lance une commande sans bloquer le terminal."""
    try:
        if PLATFORM == "win":
            # Expand %USERNAME% etc.
            cmd = os.path.expandvars(cmd)
            subprocess.Popen(cmd, shell=True,
                             creationflags=subprocess.DETACHED_PROCESS |
                                           subprocess.CREATE_NEW_PROCESS_GROUP)
        else:
            subprocess.Popen(cmd, shell=True,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        return True
    except Exception as e:
        print(f"  ✗ Erreur : {e}")
        return False


def open_app(key: str):
    app = APPS[key]
    cmd = app[PLATFORM]
    print(f"  → Lancement de {app['name']}…")
    if launch(cmd):
        print(f"  ✓ {app['name']} lancé !")


def open_brave_site(site_key: str):
    name, url = BRAVE_SITES[site_key]
    brave = BRAVE_CMD[PLATFORM]
    if PLATFORM == "win":
        brave = os.path.expandvars(brave)
        cmd = f'"{brave}" {url}'
    elif PLATFORM == "mac":
        cmd = f"open -a 'Brave Browser' '{url}'"
    else:
        cmd = f"{brave} {url}"
    print(f"  → Ouverture de {name} dans Brave…")
    if launch(cmd):
        print(f"  ✓ {name} ouvert !")


# ─────────────────────────────────────────────
#  MANU OU MENU A VOIR
# ─────────────────────────────────────────────
MENU_PAGE1 = """
 ▀██ ▄█▀  ██ ██▀███   ▄▄▄           ███▄ ▄███▓ █    ██  ██▓   ▄▄▄█████▓  ██▄▄▄█████▓ ▒█████   ▒█████   ██▓   
  ██▄█▒ ▒▓██▓██ ▒ ██▒▒████▄        ▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒   ▓  ██▒ ▓▒▒▓██▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒   
 ▓███▄░ ░▒██▓██ ░▄█ ▒▒██  ▀█▄      ▓██    ▓██░▓██  ▒██░▒██░   ▒ ▓██░ ▒░░▒██▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░   
 ▓██ █▄  ░██▒██▀▀█▄  ░██▄▄▄▄██     ▒██    ▒██ ▓▓█  ░██░▒██░   ░ ▓██▓ ░  ░██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░   
 ▒██▒ █▄ ░██░██▓ ▒██▒ ▓█   ▓██    ▒▒██▒   ░██▒▒▒█████▓ ░██████  ▒██▒ ░  ░██  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████
 ▒ ▒▒ ▓▒ ░▓ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█    ░░ ▒░   ░  ░ ▒▓▒ ▒ ▒ ░ ▒░▓    ▒ ░░    ░▓   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  
 ░ ░▒ ▒░  ▒   ░▒ ░ ▒░  ░   ▒▒     ░░  ░      ░ ░▒░ ░ ░ ░ ░ ▒      ░      ▒     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  
 ░ ░░ ░   ▒    ░   ░   ░   ▒       ░      ░     ░░ ░ ░   ░ ░    ░ ░      ▒   ░ ░    ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░  
 ░  ░     ░    ░           ░      ░       ░      ░         ░             ░              ░ ░      ░ ░      ░  


╔══════════════════════════════════════════════════════════════════╗   ╔══════════════════════╗
║        KIRA LAUNCHER MAIN MENU                                   ║   ║    Secondaire Menu   ║
╠══════════════════════════════════════════════════════════════════╣   ╠══════════════════════╣
║ 1  →  Discord         2  →  Riot        3  →  Epic Games         ║   ║     5,1 → Youtube    ║
╠══════════════════════════════════════════════════════════════════╣   ║     5,2 → Twitch     ║
║ 4  →  Steam           5  →  Brave       6  →  Script             ║   ║     5,3 → Netflix    ║
╠══════════════════════════════════════════════════════════════════╣   ╚══════════════════════╝   
║ 7  →  Proton VPN      8  →  Spotify     9  →  Leave              ║   
╠══════════════════════════════════════════════════════════════════╣   ╔════════════════════════════════════════╗      
║ 10  →  Visual Studio Code                                        ║   ║ B   →  Previous Page    N  →  Next Page║
╚══════════════════════════════════════════════════════════════════╝   ╚════════════════════════════════════════╝
Page 1/4
"""
MENU_PAGE2 = """
 ▀██ ▄█▀  ██ ██▀███   ▄▄▄           ███▄ ▄███▓ █    ██  ██▓   ▄▄▄█████▓  ██▄▄▄█████▓ ▒█████   ▒█████   ██▓   
  ██▄█▒ ▒▓██▓██ ▒ ██▒▒████▄        ▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒   ▓  ██▒ ▓▒▒▓██▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒   
 ▓███▄░ ░▒██▓██ ░▄█ ▒▒██  ▀█▄      ▓██    ▓██░▓██  ▒██░▒██░   ▒ ▓██░ ▒░░▒██▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░   
 ▓██ █▄  ░██▒██▀▀█▄  ░██▄▄▄▄██     ▒██    ▒██ ▓▓█  ░██░▒██░   ░ ▓██▓ ░  ░██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░   
 ▒██▒ █▄ ░██░██▓ ▒██▒ ▓█   ▓██    ▒▒██▒   ░██▒▒▒█████▓ ░██████  ▒██▒ ░  ░██  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████
 ▒ ▒▒ ▓▒ ░▓ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█    ░░ ▒░   ░  ░ ▒▓▒ ▒ ▒ ░ ▒░▓    ▒ ░░    ░▓   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  
 ░ ░▒ ▒░  ▒   ░▒ ░ ▒░  ░   ▒▒     ░░  ░      ░ ░▒░ ░ ░ ░ ░ ▒      ░      ▒     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  
 ░ ░░ ░   ▒    ░   ░   ░   ▒       ░      ░     ░░ ░ ░   ░ ░    ░ ░      ▒   ░ ░    ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░  
 ░  ░     ░    ░           ░      ░       ░      ░         ░             ░              ░ ░      ░ ░      ░ 

╔════════════════════════════════════════╗  ╔═════════════════════════╗  ╔════════════════════════════════════════╗
║                Discord                 ║  ║         Ip Tool         ║  ║            Discord Nuke Bot            ║
╠════════════════════════════════════════╣  ╠═════════════════════════╣  ╠════════════════════════════════════════╣
║ 11  →  Get Token (ID to Token)         ║  ║ 14  →  Ip Look Up       ║  ║  15  → Suppr and Add                   ║
║ 12  →  Invite Info                     ║  ╠═════════════════════════╣  ║  16  → Suppr and Add Random Name       ║
║ 13  →  Discord ID Info                 ║  ║  N   → Next Page        ║  ║  17  → Only Suppr                      ║
║ 24  →  Webhook Spammer                 ║  ║  B   → Previous Page    ║  ╚════════════════════════════════════════╝
║ 27  →  Webhook Message                 ║  ╚═════════════════════════╝                                    
║ 28  →  Token Tester                    ║
╚════════════════════════════════════════╝                     
Page 2/4
"""
MENU_PAGE3= """
 ▀██ ▄█▀  ██ ██▀███   ▄▄▄           ███▄ ▄███▓ █    ██  ██▓   ▄▄▄█████▓  ██▄▄▄█████▓ ▒█████   ▒█████   ██▓   
  ██▄█▒ ▒▓██▓██ ▒ ██▒▒████▄        ▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒   ▓  ██▒ ▓▒▒▓██▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒   
 ▓███▄░ ░▒██▓██ ░▄█ ▒▒██  ▀█▄      ▓██    ▓██░▓██  ▒██░▒██░   ▒ ▓██░ ▒░░▒██▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░   
 ▓██ █▄  ░██▒██▀▀█▄  ░██▄▄▄▄██     ▒██    ▒██ ▓▓█  ░██░▒██░   ░ ▓██▓ ░  ░██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░   
 ▒██▒ █▄ ░██░██▓ ▒██▒ ▓█   ▓██    ▒▒██▒   ░██▒▒▒█████▓ ░██████  ▒██▒ ░  ░██  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████
 ▒ ▒▒ ▓▒ ░▓ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█    ░░ ▒░   ░  ░ ▒▓▒ ▒ ▒ ░ ▒░▓    ▒ ░░    ░▓   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  
 ░ ░▒ ▒░  ▒   ░▒ ░ ▒░  ░   ▒▒     ░░  ░      ░ ░▒░ ░ ░ ░ ░ ▒      ░      ▒     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  
 ░ ░░ ░   ▒    ░   ░   ░   ▒       ░      ░     ░░ ░ ░   ░ ░    ░ ░      ▒   ░ ░    ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░  
 ░  ░     ░    ░           ░      ░       ░      ░         ░             ░              ░ ░      ░ ░      ░ 

 
╔════════════════════════════════════════╗  ╔════════════════════════════════════════╗
║             Look Up                    ║  ║                Roblox                  ║
╠════════════════════════════════════════╣  ╠════════════════════════════════════════╣
║ 18  →  Url Info                        ║  ║ 19 → Roblox ID Info                    ║
║ 21  →  Tiktok Id Info                  ║  ║ 20 → Roblox User Info                  ║
║ 22  →  Tiktok User Info                ║  ╚════════════════════════════════════════╝
║ 23  →  Instagram User Info             ║  
╚════════════════════════════════════════╝
Page 3/4
"""
MENU_PAGE4= """
 ▀██ ▄█▀  ██ ██▀███   ▄▄▄           ███▄ ▄███▓ █    ██  ██▓   ▄▄▄█████▓  ██▄▄▄█████▓ ▒█████   ▒█████   ██▓   
  ██▄█▒ ▒▓██▓██ ▒ ██▒▒████▄        ▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒   ▓  ██▒ ▓▒▒▓██▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒   
 ▓███▄░ ░▒██▓██ ░▄█ ▒▒██  ▀█▄      ▓██    ▓██░▓██  ▒██░▒██░   ▒ ▓██░ ▒░░▒██▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░   
 ▓██ █▄  ░██▒██▀▀█▄  ░██▄▄▄▄██     ▒██    ▒██ ▓▓█  ░██░▒██░   ░ ▓██▓ ░  ░██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░   
 ▒██▒ █▄ ░██░██▓ ▒██▒ ▓█   ▓██    ▒▒██▒   ░██▒▒▒█████▓ ░██████  ▒██▒ ░  ░██  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████
 ▒ ▒▒ ▓▒ ░▓ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█    ░░ ▒░   ░  ░ ▒▓▒ ▒ ▒ ░ ▒░▓    ▒ ░░    ░▓   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  
 ░ ░▒ ▒░  ▒   ░▒ ░ ▒░  ░   ▒▒     ░░  ░      ░ ░▒░ ░ ░ ░ ░ ▒      ░      ▒     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  
 ░ ░░ ░   ▒    ░   ░   ░   ▒       ░      ░     ░░ ░ ░   ░ ░    ░ ░      ▒   ░ ░    ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░  
 ░  ░     ░    ░           ░      ░       ░      ░         ░             ░              ░ ░      ░ ░      ░ 

╔═══════════════════════╗
║          App          ║
╠═══════════════════════╣
║ 25  →  Macro          ║
║ 26  →  Apex Config    ║
╚═══════════════════════╝
Page 4/4
"""

MENUS = [MENU_PAGE1, MENU_PAGE2, MENU_PAGE3, MENU_PAGE4]
 
def show_menu(page):
    os.system("cls" if os.name == "nt" else "clear")
    print(MENUS[page - 1])

# ─────────────────────────────────────────────
#  BOUCLE PRINCIPALE MME PUT ?
# ─────────────────────────────────────────────

def main(): 
    page = 1
 
    while True:
        show_menu(page)
        raw = input("Option : ").strip()

        if raw == "9":
            break

        if raw.lower() == "n":
            if page < len(MENUS):
                page += 1
            continue
 
        if raw.lower() == "b":
            if page > 1:
                page -= 1
            continue

        # Sous-menu Brave : format "5,X"
        if "," in raw:
            parts = raw.split(",")
            if parts[0].strip() == "5" and parts[1].strip() in BRAVE_SITES:
                open_brave_site(parts[1].strip())
            else:
                print("  ✗ Option inconnue.")
            input("\nAppuie sur Entrée pour continuer…")
            continue

        # App class
        if raw in APPS:
            open_app(raw)
        else:
            print("  ✗ Option inconnue.")

        input("\nAppuie sur Entrée pour continuer…")


if __name__ == "__main__":
    main()