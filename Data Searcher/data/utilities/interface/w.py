# data/utilities/interface/w.py
# TODO: Display | Results Writer
# NOTE: Contains function j() to write results to a timestamped file.

import time
from pathlib import Path

def j(r, p_d): 
    if not p_d.exists():
        p_d.mkdir(parents=True, exist_ok=True)
    n = time.strftime("RESULTS_%Y%m%d_%H%M%S.txt")
    p = p_d / n 
    try:
        with open(p, 'w', encoding='utf-8') as f:
            for u, i, m in r:
                f.write(f"[{u}:{i}] {m}\n")
        return n
    except Exception:
        return None