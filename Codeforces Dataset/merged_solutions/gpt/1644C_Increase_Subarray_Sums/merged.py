# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        x = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n

        best = [-10**18] * (n + 1)
        best[0] = 0

        for l in range(n):
            s = 0
            for r in range(l, n):
                s += a[r]
                length = r - l + 1
                if s > best[length]:
                    best[length] = s

        ans = []
        for k in range(n + 1):
            cur = 0
            for length in range(1, n + 1):
                val = best[length] + min(k, length) * x
                if val > cur:
                    cur = val
            ans.append(str(cur))
        out.append(" ".join(ans))

    print("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
