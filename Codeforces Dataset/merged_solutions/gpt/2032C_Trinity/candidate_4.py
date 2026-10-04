# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        a.sort()

        best = 1
        r = 0
        for l in range(n):
            if r < l + 1:
                r = l + 1
            while r < n and a[l] + a[l + 1] > a[r]:
                r += 1
            best = max(best, r - l)

        ans.append(str(n - best))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
