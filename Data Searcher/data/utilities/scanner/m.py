# data/utilities/scanner/m.py
# TODO: Scanner | Core Search Methods
# NOTE: Contains the five main search functions (w, x, y, z, a) for all scan modes.
# NOTE: Authorization | NO, this file can not be modified/used as you wish.
# WARN: This is the most critical logic module. Renaming any function here could crash the program.

import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from data.utilities.scanner.f import v
from data.utilities.interface.t import d
from pystyle import Colorate, Colors

H = os.cpu_count() or 4

def w(l, q):
    z = []
    for r, _, s in os.walk(l):
        for c in s:
            z.extend(v(Path(r) / c, q))
    return z

def x(l, q):
    return w(l, q)

def y(l, q):
    r=[Path(a)/t for a,_,s in os.walk(l) for t in s]
    z=[]
    def j(u):
        b=v(u,q)
        return b
    with ThreadPoolExecutor(max_workers=H) as p:
        b=(p.submit(j,u) for u in r)
        for c in b:
            try: z.extend(c.result())
            except Exception: continue
    return list(z)

def z(l, q, j):
    c=q.lower()
    r=[]
    for u,b in j.items():
        try:
            if c in b.lower():
                p=Path(u)
                for i,m in zip(range(1,1000000), b.splitlines()):
                    if c in m.lower():
                        from data.utilities.scanner.f import T
                        try: r.append((str(p.relative_to(T)),i,m.strip()))
                        except: r.append((p.name,i,m.strip()))
        except: continue
    return r[:]

def a(l, q, o, j):
    if o > 1:
        m = Colorate.Horizontal(Colors.blue_to_purple, "database huge, using indexed scan")
        d(m)
        return z(l, q, j)
    if o > 0.1:
        m = Colorate.Horizontal(Colors.blue_to_purple, "database medium, launching threads")
        d(m)
        return y(l, q)
    m = Colorate.Horizontal(Colors.blue_to_purple, "database small, quick scan is good")
    d(m)
    return w(l, q)