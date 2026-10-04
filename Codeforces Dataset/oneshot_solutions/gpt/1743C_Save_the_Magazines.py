import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    p = 1
    out = []

    for _ in range(t):
        n = int(data[p])
        p += 1
        s = data[p]
        p += 1
        a = list(map(int, data[p:p + n]))
        p += n

        ans = 0
        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue

            l = i
            total = 0
            mn = 10 ** 18

            if l > 0:
                total += a[l - 1]
                mn = min(mn, a[l - 1])

            while i < n and s[i] == '1':
                total += a[i]
                mn = min(mn, a[i])
                i += 1

            if l == 0:
                ans += total
            else:
                ans += total - mn

        out.append(str(ans))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
