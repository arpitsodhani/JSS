# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n, k = data[0], data[1]
    idx = 2
    keep = 0

    for _ in range(k):
        m = data[idx]
        idx += 1
        chain = data[idx:idx + m]
        idx += m

        if chain[0] == 1:
            keep = 1
            while keep < m and chain[keep] == chain[keep - 1] + 1:
                keep += 1

    print(2 * (n - keep) - (k - 1))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
