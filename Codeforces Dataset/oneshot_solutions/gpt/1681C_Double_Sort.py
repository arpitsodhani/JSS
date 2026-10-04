import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        b = data[idx:idx + n]
        idx += n

        cur = list(zip(a, b))
        target = sorted(cur)

        ok = True
        for i in range(1, n):
            if target[i][1] < target[i - 1][1]:
                ok = False
                break

        if not ok:
            out.append("-1")
            continue

        ans = []
        cur = cur[:]

        for i in range(n):
            if cur[i] == target[i]:
                continue
            j = i + 1
            while j < n and cur[j] != target[i]:
                j += 1
            cur[i], cur[j] = cur[j], cur[i]
            ans.append((i + 1, j + 1))

        out.append(str(len(ans)))
        for x, y in ans:
            out.append(f"{x} {y}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
