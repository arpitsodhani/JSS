# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def phi(x):
    res = x
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            res -= res // p
        p += 1 if p == 2 else 2
    if x > 1:
        res -= res // x
    return res

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    y = data[1].strip()
    divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
        i += 1
    ans = 0
    bits = [1 if c == '1' else 0 for c in y]
    for d in divs:
        ok = True
        parity = [0] * d
        for i, b in enumerate(bits):
            parity[i % d] ^= b
        for v in parity:
            if v:
                ok = False
                break
        if ok:
            if d == n:
                ans += 1
            else:
                ans += phi(n // d)
    print(ans)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
