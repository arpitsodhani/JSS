# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.read().strip().split()
    if not raw:
        return
    n, w, m = (int(x) for x in raw[:3])
    if m > 2 * n or m // gcd(n, m) > 2:
        print("NO")
        return
    lines = ["YES"]
    cup_size = n * w / m
    if m > n:
        x = cup_size
        lines.extend(f"1 {i} {x:.6f}" for i in range(1, n + 1) for _ in range(2))
    else:
        bottle = 1
        consumed = 0.0
        for cup in range(m):
            target = (cup + 1) * cup_size
            pieces = []
            while consumed + 1e-9 < target:
                bottle_end = bottle * w
                nxt = target if target < bottle_end else bottle_end
                pieces.append((bottle, nxt - consumed))
                consumed = nxt
                if consumed + 1e-9 >= bottle_end:
                    bottle += 1
            text = [str(len(pieces))]
            for index, value in pieces:
                text.extend((str(index), f"{value:.6f}"))
            lines.append(" ".join(text))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
