# data/utilities/interface/v.py
# TODO: Display | Interface Utility
# NOTE: Contains function g() for adding visual separation (loading effect).
# TODO: Authorization | YES, you can use this function as you wish.

import sys
import time
import random

def g():
    h = random.randint(2, 6)
    p = [".  ", ".. ", "..."]

    for i in range(h):
        for c in p:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.12)
            sys.stdout.write('\r')
            sys.stdout.flush()