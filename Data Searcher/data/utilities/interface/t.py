# data/utilities/interface/t.py
# TODO: Display | Typing Effect
# NOTE: Simple slow typer for more dynamic.
# TODO: Authorization | YES, you can use this function as you wish.

# TYPING_DELAY = 0.02
# def slowTyper(txt, end="\n"):
#     for char in txt:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(TYPING_DELAY)
#
#     sys.stdout.write(end)
#     sys.stdout.flush()

import sys
import time
from pystyle import Colorate, Colors

R = 0.0002 # Typing Delay

def d(q, x="\n"):
    for c in q:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(R)
    sys.stdout.write(x)
    sys.stdout.flush()