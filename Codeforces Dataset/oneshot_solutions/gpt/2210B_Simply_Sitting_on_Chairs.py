import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    pos = 1
    ans = []

    for _ in range(t):
        n = data[pos]
        pos += 1
        p = data[pos:pos + n]
        pos += n

        safe = [0] * (n + 1)
        for i, x in enumerate(p, 1):
            safe[i] = safe[i - 1] + (1 if x <= i else 0)

        best = safe[n]
        for i, x in enumerate(p, 1):
            if x > i:
                cur = safe[x - 1] + 1
                if cur > best:
                    best = cur

        ans.append(str(best))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
