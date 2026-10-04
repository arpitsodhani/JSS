import sys
from math import isqrt

def factorize(x):
    factors = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            cnt = 0
            while x % d == 0:
                x //= d
                cnt += 1
            factors.append((d, cnt))
        d += 1 if d == 2 else 2
    if x > 1:
        factors.append((x, 1))
    return factors

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n, m = data[0], data[1]
    a = data[2:2 + n]
    b = data[2 + n:2 + n + m]
    
    numerator = {}
    denominator = {}
    
    for x in a:
        for p, cnt in factorize(x):
            numerator[p] = numerator.get(p, 0) + cnt
    
    for x in b:
        for p, cnt in factorize(x):
            denominator[p] = denominator.get(p, 0) + cnt
    
    for p in list(numerator.keys()):
        common = min(numerator[p], denominator.get(p, 0))
        numerator[p] -= common
        denominator[p] = denominator.get(p, 0) - common
    
    new_a = []
    for x in a:
        value = 1
        for p, cnt in factorize(x):
            take = min(cnt, numerator.get(p, 0))
            if take:
                value *= p ** take
                numerator[p] -= take
        new_a.append(value)
    
    new_b = []
    for x in b:
        value = 1
        for p, cnt in factorize(x):
            take = min(cnt, denominator.get(p, 0))
            if take:
                value *= p ** take
                denominator[p] -= take
        new_b.append(value)
    
    print(n, m)
    print(' '.join(map(str, new_a)))
    print(' '.join(map(str, new_b)))

if __name__ == "__main__":
    main()
