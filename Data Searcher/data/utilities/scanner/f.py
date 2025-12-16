# data/utilities/scanner/f.py
# TODO: Scanner | Fragmented Configuration/Constants
# NOTE: Contains configuration variables and constants (V_T) used by the scanner modules.
# NOTE: Authorization | NO, this file can not be modified/used as you wish.

from pathlib import Path

T = Path("data") / "datums" 

def v(u, q):
    z=[]
    try:
        with u.open("r",encoding="utf-8",errors="ignore") as h:
            for a,l in zip(range(1,1000000), h):
                if q.lower() in l.lower():
                    try:
                        r=str(u.relative_to(T))
                        z.append((r,a,l.strip()))
                    except Exception:
                        z.append((u.name,a,l.strip()))
    except Exception: pass
    return z[:]