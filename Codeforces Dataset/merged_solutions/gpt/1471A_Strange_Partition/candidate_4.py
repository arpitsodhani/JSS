# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        x = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n

        total = sum(a)
        mn = (total + x - 1) // x
        mx = sum((v + x - 1) // x for v in a)
        out.append(f"{mn} {mx}")

    print("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
