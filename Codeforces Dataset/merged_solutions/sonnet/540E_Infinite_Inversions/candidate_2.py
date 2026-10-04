# CLAUSE: setup_environment
import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    pos = 1
    current = {}
    touched = set()

# CLAUSE: solve_logic
    for _ in range(n):
        a = data[pos]
        b = data[pos + 1]
        pos += 2
        va = current.get(a, a)
        vb = current.get(b, b)
        current[a] = vb
        current[b] = va
        touched.add(a)
        touched.add(b)

    coords = sorted(touched)
    m = len(coords)
    bit = [0] * (m + 1)

    def add(i):
        while i <= m:
            bit[i] += 1
            i += i & -i

    def prefix(i):
        s = 0
        while i:
            s += bit[i]
            i -= i & -i
        return s

    ans = 0
    for i, x in enumerate(coords):
        y = current.get(x, x)
        r = bisect_left(coords, y) + 1
        ans += i - prefix(r)
        add(r)

    for x in coords:
        y = current.get(x, x)
        if x != y:
            lx = bisect_left(coords, x)
            ly = bisect_left(coords, y)
            ans += abs(y - x) - abs(ly - lx)

# CLAUSE: finish_program
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    main()
