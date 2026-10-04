# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    q = int(data[2])

    ans = [[0] * (n + 1) for _ in range(26)]

    for ch in range(26):
        target = chr(ord('a') + ch)
        best = ans[ch]
        for l in range(n):
            changes = 0
            for r in range(l, n):
                if s[r] != target:
                    changes += 1
                if changes > n:
                    break
                length = r - l + 1
                if length > best[changes]:
                    best[changes] = length
        for m in range(1, n + 1):
            if best[m - 1] > best[m]:
                best[m] = best[m - 1]

    out = []
    idx = 3
    for _ in range(q):
        m = int(data[idx])
        c = data[idx + 1]
        idx += 2
        out.append(str(ans[ord(c) - ord('a')][min(m, n)]))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
