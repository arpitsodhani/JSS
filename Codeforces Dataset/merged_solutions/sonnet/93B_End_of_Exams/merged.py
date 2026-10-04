# Clause setup_environment [Confidence: 0.60]
import sys
from math import gcd


# Clause solve_logic [Confidence: 0.60]
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, w, m = map(int, data[:3])
    g = gcd(n, m)
    if m > 2 * n or m // g > 2:
        print("NO")
        return
    out = ["YES"]
    each = n * w / m
    if m <= n:
        bottle = 1
        rest = float(w)
        for _ in range(m):
            need = each
            row = []
            while need > 1e-9:
                take = rest if rest < need else need
                row.append((bottle, take))
                need -= take
                rest -= take
                if rest < 1e-9:
                    bottle += 1
                    rest = float(w)
            line = [str(len(row))]
            for b, x in row:
                line.append(str(b))
                line.append(f"{x:.6f}")
            out.append(" ".join(line))
    else:
        half = w / 2
        for b in range(1, n + 1):
            out.append(f"1 {b} {half:.6f}")
            out.append(f"1 {b} {half:.6f}")
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.40]
main()


