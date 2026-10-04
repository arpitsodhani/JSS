# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ans = []

    idx = 1
    for _ in range(t):
        k = data[idx]
        m = data[idx + 1]
        idx += 2

        r = m % (3 * k)
        if 2 * k <= r < 3 * k:
            ans.append("0")
        elif r < 2 * k:
            ans.append(str(2 * k - r))
        else:
            ans.append(str(0))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
