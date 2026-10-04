# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    pos = 1
    ans = []

    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2

        x = 0
        while (x + 1) * (x + 2) // 2 <= k:
            x += 1

        rem = k - x * (x + 1) // 2
        a = [2] * x

        if x < n:
            if rem == 0:
                a.append(-1000)
            else:
                a.append(-(2 * (x - rem) + 1))

        while len(a) < n:
            a.append(-1000)

        ans.append(" ".join(map(str, a)))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
