# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]
    m = data[1 + n]
    q = data[2 + n:2 + n + m]

    a.sort()
    total = sum(a)

    out = []
    for x in q:
        out.append(str(total - a[n - x]))

    print("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
