# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ans = []

    for i in range(1, t + 1):
        n = data[i]
        arr = list(range(n, 0, -1)) + [n] + list(range(1, n))
        ans.append(" ".join(map(str, arr)))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
