# data/utilities/scanner/i.py
# TODO: Scanner | Indexing Logic
# NOTE: Contains function n(S) which builds the searchable index (J) used by Indexed Scan.
# NOTE: Authorization | NO, this file can not be modified/used as you wish.

import os
from pathlib import Path

def n(l):
    j={}
    for q,r,s in os.walk(l):
        for t in s:
            u=Path(q)/t
            b=""
            try:
                with u.open("r",encoding="utf-8",errors="ignore") as h:
                    b=h.read()
                    j[str(u)]=b
            except: continue
    return dict(j)