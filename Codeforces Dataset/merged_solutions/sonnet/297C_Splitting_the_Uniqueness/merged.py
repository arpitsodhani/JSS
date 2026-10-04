# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n = values[0]
    s = values[1:1 + n]
    order = sorted(range(n), key=s.__getitem__)

    a = [0] * n
    b = [0] * n
    used_b = set()

    for rank, index in enumerate(order):
        remaining = s[index] - rank
        if remaining < 0 or remaining in used_b:
            sys.stdout.write("NO\n")
            return
        a[index] = rank
        b[index] = remaining
        used_b.add(remaining)

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, a)) + "\n")
    sys.stdout.write(" ".join(map(str, b)) + "\n")


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


