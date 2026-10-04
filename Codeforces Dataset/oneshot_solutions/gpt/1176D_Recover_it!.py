import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    b = data[1:]
    m = max(b)

    spf = [0] * (m + 1)
    primes = []
    pos = [0] * (m + 1)

    for i in range(2, m + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            pos[i] = len(primes)
        for p in primes:
            v = i * p
            if v > m or p > spf[i]:
                break
            spf[v] = p

    cnt = Counter(b)
    ans = []

    for x in sorted(b, reverse=True):
        if cnt[x] == 0:
            continue
        cnt[x] -= 1
        if spf[x] == x:
            y = pos[x]
            ans.append(y)
            cnt[y] -= 1
        else:
            ans.append(x)
            y = x // spf[x]
            cnt[y] -= 1

    print(*ans[:n])

if __name__ == "__main__":
    main()
