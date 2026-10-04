# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def possible(n, m):
    return m <= 2 * n and m // gcd(n, m) <= 2

def line_from(parts):
    return " ".join([str(len(parts))] + [item for b, a in parts for item in (str(b), f"{a:.6f}")])

def fill_many_bottles(n, w, m):
    size = n * w / m
    result = []
    bottle = 1
    remaining = float(w)
    cup = 0
    while cup < m:
        want = size
        parts = []
        while want > 1e-9:
            amount = min(want, remaining)
            parts.append((bottle, amount))
            want -= amount
            remaining -= amount
            if remaining <= 1e-9:
                bottle += 1
                remaining = float(w)
        result.append(line_from(parts))
        cup += 1
    return result

def fill_halves(n, w):
    amount = w / 2.0
    rows = []
    for bottle in range(1, n + 1):
        rows.append(line_from([(bottle, amount)]))
        rows.append(line_from([(bottle, amount)]))
    return rows

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, w, m = map(int, data[:3])
    if not possible(n, m):
        sys.stdout.write("NO")
        return
    rows = ["YES"]
    rows += fill_many_bottles(n, w, m) if m <= n else fill_halves(n, w)
    sys.stdout.write("\n".join(rows))

# CLAUSE: finish_program
main()
