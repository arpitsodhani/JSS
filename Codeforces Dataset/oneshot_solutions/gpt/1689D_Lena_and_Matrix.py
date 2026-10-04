import sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2

        max_sum = -10**18
        min_sum = 10**18
        max_diff = -10**18
        min_diff = 10**18

        for i in range(1, n + 1):
            row = data[idx]
            idx += 1
            for j, ch in enumerate(row, 1):
                if ch == 'B':
                    s = i + j
                    d = i - j
                    max_sum = max(max_sum, s)
                    min_sum = min(min_sum, s)
                    max_diff = max(max_diff, d)
                    min_diff = min(min_diff, d)

        best = 10**18
        ans = (1, 1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = i + j
                d = i - j
                cur = max(
                    abs(s - max_sum),
                    abs(s - min_sum),
                    abs(d - max_diff),
                    abs(d - min_diff)
                )
                if cur < best:
                    best = cur
                    ans = (i, j)

        out.append(f"{ans[0]} {ans[1]}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
