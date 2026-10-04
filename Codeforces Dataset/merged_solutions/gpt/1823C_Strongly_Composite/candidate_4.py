# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from math import isqrt
    from collections import defaultdict

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1

    tests = []
    mx = 0
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        tests.append(arr)
        if arr:
            mx = max(mx, max(arr))

    limit = isqrt(mx) + 1
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    primes = []
    for i in range(2, limit + 1):
        if sieve[i]:
            primes.append(i)
            step = i
            start = i * i
            if start <= limit:
                sieve[start:limit + 1:step] = b'\x00' * (((limit - start) // step) + 1)

    out = []
    for arr in tests:
        cnt = defaultdict(int)

        for x in arr:
            v = x
            for p in primes:
                if p * p > v:
                    break
                while v % p == 0:
                    cnt[p] += 1
                    v //= p
            if v > 1:
                cnt[v] += 1

        ans = 0
        rem = 0
        for c in cnt.values():
            ans += c // 2
            rem += c % 2
        ans += rem // 3
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
