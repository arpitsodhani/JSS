import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    t = int(data[0])
    p = 1
    ans = []

    for _ in range(t):
        n = int(data[p])
        p += 1

        genres = []
        writers = []
        for _ in range(n):
            genres.append(data[p])
            writers.append(data[p + 1])
            p += 2

        adj = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if genres[i] == genres[j] or writers[i] == writers[j]:
                    adj[i] |= 1 << j
                    adj[j] |= 1 << i

        full = (1 << n) - 1
        dp = [0] * (1 << n)

        for i in range(n):
            dp[1 << i] = 1 << i

        best = 1

        for mask in range(1 << n):
            lasts = dp[mask]
            if not lasts:
                continue

            cnt = mask.bit_count()
            if cnt > best:
                best = cnt

            rem = full ^ mask
            while lasts:
                lb = lasts & -lasts
                i = lb.bit_length() - 1
                nxt = adj[i] & rem

                while nxt:
                    nb = nxt & -nxt
                    j = nb.bit_length() - 1
                    dp[mask | nb] |= nb
                    nxt -= nb

                lasts -= lb

        ans.append(str(n - best))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
