import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n, k, b, s = data[idx:idx + 4]
        idx += 4

        minimum = b * k
        maximum = minimum + n * (k - 1)

        if s < minimum or s > maximum:
            out.append("-1")
            continue

        ans = [0] * n
        ans[0] = minimum
        extra = s - minimum

        add = min(extra, k - 1)
        ans[0] += add
        extra -= add

        for i in range(1, n):
            add = min(extra, k - 1)
            ans[i] = add
            extra -= add

        out.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
