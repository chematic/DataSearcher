### TODO: Data Searcher entirely made by @azunoo on Discord !
### TODO: Version: VERSION (Updater)
### TODO: Purpose: Fragmented multi-tool for data retrieval and analysis.
### TODO: License: Restricted Use - Unauthorized modification is forbidden

# NOTE: The entire script has been slightly obfuscated.

import os
import sys
import time
import json
from pathlib import Path
from pystyle import Colorate, Colors

from data.utilities.interface.t import d
from data.utilities.interface.v import g
from data.utilities.interface.h import i
from data.utilities.interface.w import j
from data.utilities.scanner.s import k
from data.utilities.scanner.i import n
from data.utilities.scanner.f import T as V_T
from data.utilities.scanner.m import w, x, y, z, a

try:
    from data import c 
    _UPDATER_LOADED = True 
except ImportError:
    print(f"[{time.strftime('%H:%M:%S')}] [WARN] Updater module 'c.py' fail to load. Running with no update check.")
    
    class MockUpdater:
        def s(self):
            return (G, None)
    c = MockUpdater()
    _UPDATER_LOADED = False

S = Path("data") / "datums"
L = Path("data") / "saves"
H = os.cpu_count() or 4
J = {}
V_T = S
G = "00001"

def THE_TERMS_OF_USE():
    inits = Path("data") / "xxxxx"
    terms = Path("data") / "terms"
    try:
        if not inits.exists():
            if terms.exists():
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=" * 64)
                print("INITIAL SOFTWARE LAUNCH - TERMS OF USE")
                print("=" * 64)
                with open(terms, 'r') as f:
                    print(f.read())
                print("-" * 64)
                print("The software will proceed in 10 seconds. Press Ctrl+C to stop.")
                print("-" * 64)
                time.sleep(10)
                with open(inits, 'w') as f:
                    f.write(str(time.time()))
                os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

def m():
    THE_TERMS_OF_USE()
    
    global G
    
    r_v, r_n = G, None 
    
    if _UPDATER_LOADED:
        try:
            r_v, r_n = c.s() 
        except Exception as update_err:
            print(f"[{time.strftime('%H:%M:%S')}] [ERROR] Update failed: {update_err}. Launching without checking updates.")

    G = r_v
    
    if r_n:
        sys.exit(0)
        
    if not S.exists():
        S.mkdir(parents=True, exist_ok=True)
        q = Colorate.Horizontal(Colors.blue_to_purple, "folder 'data/datums' not found, created one")
        d(q); g()

    if not L.exists():
        L.mkdir(parents=True, exist_ok=True)
        q = Colorate.Horizontal(Colors.blue_to_purple, "folder 'data/saves' not found, created one")
        d(q); g()
        
    o, f, p = k(S)
    
    r_h = i(o, f, p, G)
    print(r_h) 
    print("-" * 64)

    q = Colorate.Horizontal(Colors.blue_to_purple, "what do u want to search now? >> ")
    d(q, x="")
    c_input = input().strip()
    
    g()
    
    r_msg = Colorate.Horizontal(Colors.blue_to_purple, f'request: "{c_input}"')
    d(r_msg)
    
    if not c_input:
        q = Colorate.Horizontal(Colors.blue_to_purple, "request empty, closing")
        d(q)
        return

    e = {
        "1": ("Simple Scan", w),
        "2": ("Deep Scan", x),
        "3": ("Threaded Scan", y),
        "4": ("Indexed Scan", z),
        "A": ("Auto Mode", a)
    }

    d(Colorate.Horizontal(Colors.blue_to_purple, "\nyour options:"))
    for k_opt, (l, _) in e.items():
        d(Colorate.Horizontal(Colors.blue_to_purple, f"[{k_opt}] {l}"))
    print("-" * 64)

    q = Colorate.Horizontal(Colors.blue_to_purple, "pick any methods >> ")
    d(q, x="")
    k_input = input().upper().strip()

    if k_input not in e:
        q = Colorate.Horizontal(Colors.blue_to_purple, "unvalid option, choosing auto")
        d(q)
        k_input = "A"

    l, t = e[k_input]
    r_start = Colorate.Horizontal(Colors.blue_to_purple, f"\nsearching for '{c_input}' using {l}...")
    d(r_start)

    w_time = time.time()
    r = None

    try:
        if k_input == "4" or (k_input == "A" and o > 1):
            global J
            q = Colorate.Horizontal(Colors.blue_to_purple,"making an index of everything, pls wait")
            d(q)
            J=n(S)
            q = Colorate.Horizontal(Colors.blue_to_purple,"index is ready to use")
            d(q)
        
        if k_input == "A":
            r = t(S, c_input, o, J)
        elif k_input == "4":
            r = t(S, c_input, J)
        else:
            r = t(S, c_input)
    except Exception as j_err:
        r_err = Colorate.Horizontal(Colors.blue_to_purple, f"critical error: {j_err}")
        d(r_err)
        return

    v = time.time() - w_time
    print("-" * 64)

    if r:
        u = len({a_file[0] for a_file in r})
        r_summary = Colorate.Horizontal(Colors.blue_to_purple, f"success! Found {len(r)} matches across {u} files in {v:.4f}s.")
        d(r_summary)
        d(Colorate.Horizontal(Colors.blue_to_purple, "\nResults:"))
        
        for a_file, b_line, l_res in r[:20]:
            r_line = Colorate.Horizontal(Colors.blue_to_purple, f"[{a_file}:{b_line}] {l_res}")
            print(r_line)
            
        if len(r) > 20:
            r_rem = Colorate.Horizontal(Colors.blue_to_purple, f"...\n(showing only the first 20 results out of {len(r)})")
            print(r_rem)
            
        print("-" * 64)
        
        q = Colorate.Horizontal(Colors.blue_to_purple, "do u want to save all results to data/saves? (Y/N) >> ")
        d(q, x="")
        save_input = input().upper().strip()

        if save_input == 'Y':
            file_name = j(r, L)
            if file_name:
                q = Colorate.Horizontal(Colors.blue_to_purple, f"all results saved to {L / file_name}")
                d(q)
            else:
                q = Colorate.Horizontal(Colors.blue_to_purple, "error: failed to save results.")
                d(q)
    else:
        r_fail = Colorate.Horizontal(Colors.blue_to_purple, f"failure, nothing matched '{c_input}', search done in {v:.4f}s.")
        d(r_fail)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        m()
    except KeyboardInterrupt:
        r_exit = Colorate.Horizontal(Colors.blue_to_purple, "\nsearch canceled. see you later!")
        d(r_exit)
    except Exception as e:
        r_fatal = Colorate.Horizontal(Colors.blue_to_purple, f"\nfatal error: {e}")
        d(r_fatal)
        time.sleep(1)