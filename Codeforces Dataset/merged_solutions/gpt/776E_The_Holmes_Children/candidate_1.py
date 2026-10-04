# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
MOD = 1000000007

def build_primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    r = int(limit ** 0.5)
    for i in range(2, r + 1):
        if sieve[i]:
            start = i * i
            sieve[start:limit + 1:i] = b'\x00' * (((limit - start) // i) + 1)
    return [i for i in range(2, limit + 1) if sieve[i]]

def phi(x, primes):
    res = x
    t = x
    for p in primes:
        if p * p > t:
            break
        if t % p == 0:
            res = res // p * (p - 1)
            while t % p == 0:
                t //= p
    if t > 1:
        res = res // t * (t - 1)
    return res

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])

    primes = build_primes(math.isqrt(n) + 1)
    steps = (k + 1) // 2

    while steps and n > 1:
        n = phi(n, primes)
        steps -= 1

    print(n % MOD)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
