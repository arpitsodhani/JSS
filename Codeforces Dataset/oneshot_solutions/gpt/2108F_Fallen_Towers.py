import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    out = []

    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n

        def check(ans):
            d = [0] * (n + 1)
            acc = 0
            base = n - ans

            for i, ai in enumerate(a):
                acc -= d[i]
                need = i - base
                if need < 0:
                    need = 0
                if acc < need:
                    return False

                end = i + ai + acc - need + 1
                acc += 1
                if end < n:
                    d[end] += 1

            return True

        lo, hi = 1, n + 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid

        out.append(str(lo))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
