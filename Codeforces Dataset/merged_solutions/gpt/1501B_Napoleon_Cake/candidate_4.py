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
        idx += 1
        a = data[idx:idx + n]
        idx += n

        ans = [0] * n
        cream = 0

        for i in range(n - 1, -1, -1):
            cream = max(cream, a[i])
            if cream > 0:
                ans[i] = 1
                cream -= 1

        out.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
