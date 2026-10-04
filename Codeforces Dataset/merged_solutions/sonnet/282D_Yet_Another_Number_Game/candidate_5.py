# CLAUSE: setup_environment
import sys
from math import isqrt

# CLAUSE: solve_logic
def wythoff(a, b):
    lo = min(a, b)
    hi = max(a, b)
    d = hi - lo
    if not d:
        return not lo
    root_part = isqrt(5) if d == 1 else isqrt(5 * d * d)
    return lo == (d + root_part) // 2

def compute_answer(items):
    size = items[0]
    seq = items[1:1 + size]
    if size == 1:
        first_wins = bool(seq[0])
    elif size == 2:
        first_wins = not wythoff(seq[0], seq[1])
    else:
        first_wins = False
        acc = 0
        for number in seq:
            acc = acc ^ number
        first_wins = acc != 0
    return ("BitAryo", "BitLGM")[first_wins]

# CLAUSE: finish_program
content = sys.stdin.buffer.read().split()
if content:
    parsed = tuple(map(int, content))
    print(compute_answer(parsed))
