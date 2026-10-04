import sys
from math import gcd

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2

        a = data[idx:idx + n]
        idx += n

        g = 0
        for x in data[idx:idx + m]:
            g = gcd(g, x)
        idx += m

        even_total = 0
        odd_total = 0

        for r in range(g):
            s = 0
            parity = 0
            mn = 10**30

            for i in range(r, n, g):
                v = a[i]
                if v < 0:
                    parity ^= 1
                    v = -v
                s += v
                if v < mn:
                    mn = v

            if parity == 0:
                even_total += s
                odd_total += s - 2 * mn
            else:
                even_total += s - 2 * mn
                odd_total += s

        out.append(str(max(even_total, odd_total)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
