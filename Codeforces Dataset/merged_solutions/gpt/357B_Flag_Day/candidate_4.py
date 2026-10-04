# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    colors = [0] * (n + 1)
    p = 2

    for _ in range(m):
        dancers = data[p:p + 3]
        p += 3

        used = {colors[x] for x in dancers if colors[x] != 0}
        available = [c for c in (1, 2, 3) if c not in used]

        for x in dancers:
            if colors[x] == 0:
                colors[x] = available.pop()

    print(*colors[1:])

# CLAUSE: finish_program
def main():
    _inner_main()

main()
