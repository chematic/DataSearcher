## data/c.py
## TODO: STANDALONE Auto Updater
## TODO: Unique Updater: The code c.py is considered stable and will remain unchanged FOR NOW.
## NOTE: Function c.s() handles GitHub API requests for version control and update delivery.
## NOTE: Authorization | NO, you cannot modify/use this function as you wish.

import urllib.request
import urllib.error
import ssl
import json
from data.utilities.interface.t import d
from pystyle import Colorate, Colors
from pathlib import Path

J = "https://api.github.com/repos/chematic/DataSearcher/releases/latest"
SCANNER_PATH = Path("data") / "utilities" / "scanner"
INTERFACE_PATH = Path("data") / "utilities" / "interface"

def b(filename):
    p_scanner = SCANNER_PATH / filename
    p_interface = INTERFACE_PATH / filename
    
    if p_scanner.exists():
        return p_scanner
    if p_interface.exists():
        return p_interface
    
    return None

def a(q, r):
    if not r: return False
    
    try:
        q_num = int(q.strip().lstrip('v'))
        r_num = int(r.strip().lstrip('v'))
        
        return r_num > q_num
    except ValueError:
        return False

def c(L):
    H = J
    B = ssl._create_unverified_context()
    T = None
    update_performed = False

    try:
        with urllib.request.urlopen(H, context=B, timeout=3) as P:
            R = P.read().decode('utf-8')
            S = json.loads(R)
            T = S.get('tag_name', L)
            
            if a(L, T):
                
                q_consent = Colorate.Horizontal(Colors.blue_to_purple, f"[ALERT] New version {T} available! Update files? (Y/N) >> ")
                d(q_consent, x="")
                consent = input().upper().strip()
                
                if consent != 'Y':
                    d(Colorate.Horizontal(Colors.blue_to_purple, "Update aborted by user."))
                    return None
                
                for asset in S.get('assets', []):
                    U = asset.get('browser_download_url')
                    F = asset.get('name')
                    L_PATH = b(F)

                    if L_PATH:
                        message = Colorate.Horizontal(Colors.blue_to_purple, f"Starting update for {F}...")
                        d(message)

                        try:
                            req = urllib.request.Request(U, headers={'User-Agent' : 'Mozilla/5.0'})
                            download = urllib.request.urlopen(req, context=B, timeout=5).read()
                            
                            with open(L_PATH, "wb") as f:
                                f.write(download)
                            
                            message = Colorate.Horizontal(Colors.blue_to_purple, f"Update for {F} successful.")
                            d(message)
                            update_performed = True
                            
                        except Exception as e:
                            message = Colorate.Horizontal(Colors.blue_to_purple, f"[CRITICAL ERROR] Failed to write {F} at {L_PATH}: {e}")
                            d(message)
                    else:
                        message = Colorate.Horizontal(Colors.red, f"[CRITICAL ERROR] Remote file {F} not found locally! Check file structure.")
                        d(message)

                if update_performed:
                    message = Colorate.Horizontal(Colors.blue_to_purple, f"All updates applied. Updating local version to {T}.")
                    d(message)
                    
                    with open("VERSION", "w") as f:
                        f.write(T.lstrip('v'))
                        
                    return T
                
    except urllib.error.URLError as e:
        pass
    except Exception as e:
        pass
        
    return None

def s():
    L = "00000"
    try:
        with open("VERSION", 'r') as f:
            L = f.read().strip()
    except Exception:
        pass
        
    T = c(L)
    
    return (L, T)