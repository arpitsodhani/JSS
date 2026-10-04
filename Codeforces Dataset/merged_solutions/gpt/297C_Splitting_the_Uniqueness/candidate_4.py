# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    s = data[1:1 + n]

    items = sorted((x, i) for i, x in enumerate(s))
    a = [0] * n
    b = [0] * n

    p = n // 3
    q = (2 * n) // 3

    for pos, (val, idx) in enumerate(items):
        if pos < p:
            a[idx] = pos
            b[idx] = val - pos
        elif pos < q:
            b[idx] = pos
            a[idx] = val - pos
        else:
            b[idx] = n - 1 - pos
            a[idx] = val - b[idx]

    out = ["YES", " ".join(map(str, a)), " ".join(map(str, b))]
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
