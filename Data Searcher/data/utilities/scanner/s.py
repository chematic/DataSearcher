# data/utilities/scanner/s.py
# TODO: Scanner | Directory Analysis
# NOTE: Contains function k(S) which performs initial analysis of the data folder (file count, size, etc.).
# NOTE: Authorization | NO, this file can not be modified/used as you wish.

import os
from pathlib import Path

def k(l):
    z=0; y=0; x=0
    if not l.exists(): l.mkdir(parents=True, exist_ok=True)
    for q,r,s in os.walk(l):
        x+=len(r)
        for t in s:
            u=Path(q)/t
            try:
                z+=u.stat().st_size
                y+=1
            except Exception: continue
    return list((z/(1024**3), y, x))