# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def numbers():
    data = sys.stdin.buffer.read()
    value = 0
    active = False
    for ch in data:
        if 48 <= ch <= 57:
            value = value * 10 + ch - 48
            active = True
        elif active:
            yield value
            value = 0
            active = False
    if active:
        yield value

def main():
    it = numbers()
    n = next(it)
    m = next(it)
    total = n * m
    base = total
    cells = []
    for i in range(n):
        row_base = i * m
        for j in range(m):
            cells.append(next(it) * base + row_base + j)
    r = next(it) - 1
    c = next(it) - 1
    target = r * m + c
    cells.sort()

    inv = [0] * (total + 1)
    if total:
        inv[1] = 1
    for i in range(2, total + 1):
        inv[i] = (MOD - (MOD // i) * inv[MOD % i] % MOD) % MOD

    count = 0
    sx = 0
    sy = 0
    ss = 0
    sd = 0
    ans = 0
    p = 0

    while p < total:
        v = cells[p] // base
        q = p + 1
        while q < total and cells[q] // base == v:
            q += 1

        gx = 0
        gy = 0
        gs = 0
        gd = 0

        if count:
            inv_count = inv[count]
            for t in range(p, q):
                idx = cells[t] % base
                x = idx // m + 1
                y = idx % m + 1
                z = x * x + y * y
                cur = (sd + count * z - 2 * x * sx - 2 * y * sy + ss) % MOD
                cur = cur * inv_count % MOD
                if idx == target:
                    ans = cur
                gx = (gx + x) % MOD
                gy = (gy + y) % MOD
                gs = (gs + z) % MOD
                gd = (gd + cur) % MOD
        else:
            for t in range(p, q):
                idx = cells[t] % base
                x = idx // m + 1
                y = idx % m + 1
                z = x * x + y * y
                if idx == target:
                    ans = 0
                gx = (gx + x) % MOD
                gy = (gy + y) % MOD
                gs = (gs + z) % MOD

        count += q - p
        sx = (sx + gx) % MOD
        sy = (sy + gy) % MOD
        ss = (ss + gs) % MOD
        sd = (sd + gd) % MOD
        p = q

    sys.stdout.write(str(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
