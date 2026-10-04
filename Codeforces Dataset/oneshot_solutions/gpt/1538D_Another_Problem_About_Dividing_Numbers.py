import sys
import math

def build_primes(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            start = i * i
            sieve[start:limit + 1:i] = b"\x00" * (((limit - start) // i) + 1)
    return [i for i in range(limit + 1) if sieve[i]]

PRIMES = build_primes(31623)

def omega(n):
    cnt = 0
    for p in PRIMES:
        if p * p > n:
            break
        while n % p == 0:
            n //= p
            cnt += 1
    if n > 1:
        cnt += 1
    return cnt

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    idx = 1
    for _ in range(t):
        a, b, k = data[idx], data[idx + 1], data[idx + 2]
        idx += 3

        if k == 1:
            out.append("YES" if a != b and (a % b == 0 or b % a == 0) else "NO")
        else:
            out.append("YES" if k <= omega(a) + omega(b) else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
