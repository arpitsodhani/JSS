import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        d = data[pos + 2]
        pos += 3
        p = data[pos:pos + n]
        pos += n
        a = data[pos:pos + m]
        pos += m
        cases.append((d, p, a))
    return cases

# Clause least_moves [Confidence: 1.00]
def least_moves(d, p, a):
    n = len(p)
    where = [0] * (n + 1)
    for i in range(n):
        where[p[i]] = i + 1
    best = -1
    for i in range(len(a) - 1):
        x = where[a[i]]
        y = where[a[i + 1]]
        if x >= y or y > x + d:
            return 0
        cost = y - x
        room = (x - 1) + (n - y)
        need = d + 1 - cost
        if need <= room and need < cost:
            cost = need
        if best < 0 or cost < best:
            best = cost
    if best < 0:
        return 0
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for d, p, a in read_input():
        out.append(least_moves(d, p, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

