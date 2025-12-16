# data/utilities/interface/h.py
# TODO: Display | Header & Status Builder
# NOTE: ASCII Header for clarity + misc informations (e.g. "GB", "files" ...)
# TODO: Authorization | NO, you cannot modify/use this function as you wish.

from pystyle import Colorate, Colors

def i(o, f, p, v):
    e = f"""
████▄  █████▄   ▄█████ ▄▄▄▄▄  ▄▄▄  ▄▄▄▄   ▄▄▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  
██  ██ ██▄▄██   ▀▀▀▄▄▄ ██▄▄  ██▀██ ██▄█▄ ██▀▀▀ ██▄██ ██▄▄  ██▄█▄ 
████▀  ██▄▄█▀   █████▀ ██▄▄▄ ██▀██ ██ ██ ▀████ ██ ██ ██▄▄▄ ██ ██ 
Version: {v}
"""
    m = f": {o:.2f} GB | {f} files | {p} folders"
    
    print(Colorate.Horizontal(Colors.blue_to_purple, e).strip())
    
    return Colorate.Horizontal(Colors.blue_to_purple, m)