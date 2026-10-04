import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n, m, q = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        intervals = [(m, m)]
        ans = []

        for _ in range(q):
            a = data[idx]
            idx += 1

            new_intervals = []
            hit = False

            for l, r in intervals:
                if r < a:
                    new_intervals.append((l, min(n, r + 1)))
                elif l > a:
                    new_intervals.append((max(1, l - 1), r))
                else:
                    new_intervals.append((l, r))
                    hit = True

            if hit:
                new_intervals.append((1, 1))
                new_intervals.append((n, n))

            new_intervals.sort()
            merged = []
            for l, r in new_intervals:
                if not merged or l > merged[-1][1] + 1:
                    merged.append([l, r])
                else:
                    if r > merged[-1][1]:
                        merged[-1][1] = r

            intervals = [(l, r) for l, r in merged]
            ans.append(str(sum(r - l + 1 for l, r in intervals)))

        out.append(" ".join(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
