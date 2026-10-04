import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]

    pos = [i for i, x in enumerate(a) if x]
    total = len(pos)

    if total == 0:
        print(0)
        return
    if total == 1:
        print(-1)
        return

    x = total
    primes = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            primes.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        primes.append(x)

    ans = 10**30

    for p in primes:
        cost = 0
        for l in range(0, total, p):
            m = l + p // 2
            center = pos[m]
            for j in range(l, l + p):
                cost += abs(pos[j] - center)
        ans = min(ans, cost)

    print(ans)

if __name__ == "__main__":
    main()
