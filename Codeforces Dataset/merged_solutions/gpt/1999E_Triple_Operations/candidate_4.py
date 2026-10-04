# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def steps(n):
        c = 0
        while n:
            c += 1
            n //= 3
        return c

    def pref(n):
        if n <= 0:
            return 0
        total = 0
        p = 1
        k = 1
        while p <= n:
            q = p * 3
            total += (min(n, q - 1) - p + 1) * k
            p = q
            k += 1
        return total

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    ans = []
    idx = 1

    for _ in range(t):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        ans.append(str(pref(r) - pref(l - 1) + steps(l)))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
