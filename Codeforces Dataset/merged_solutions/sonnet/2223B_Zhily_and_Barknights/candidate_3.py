# CLAUSE: setup_environment
import sys
from collections import Counter

MOD = 998244353

class OrderedRatio:
    __slots__ = ("top", "bottom", "ways")

    def __init__(self, top, bottom, ways):
        self.top = top
        self.bottom = bottom
        self.ways = ways

    def __lt__(self, other):
        return self.top * other.bottom < other.top * self.bottom

# CLAUSE: solve_logic
def make_distribution(values):
    counted = Counter(values)
    distinct = list(counted)
    result = []
    for bottom in distinct:
        cb = counted[bottom]
        for top in distinct:
            ct = counted[top]
            ways = cb * (ct - (1 if top == bottom else 0))
            if ways:
                result.append(OrderedRatio(top, bottom, ways))
    result.sort()
    return result

def prefix_weights(ratios):
    tops = []
    bottoms = []
    pref = [0] * (len(ratios) + 1)
    for i, item in enumerate(ratios):
        tops.append(item.top)
        bottoms.append(item.bottom)
        pref[i + 1] = (pref[i] + item.ways) % MOD
    return tops, bottoms, pref

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    at = 1
    out = []
    for _ in range(data[0]):
        n = data[at]
        at += 1
        a = data[at:at + n]
        at += n
        b = data[at:at + n]
        at += n

        ratios = make_distribution(b)
        tops, bottoms, pref = prefix_weights(ratios)

        def query(x, y):
            lo = 0
            hi = len(tops)
            while lo < hi:
                mid = (lo + hi) // 2
                if tops[mid] * y < bottoms[mid] * x:
                    lo = mid + 1
                else:
                    hi = mid
            return pref[lo]

        seen = {}
        ans = 0
        for y in a:
            for x in seen:
                ans = (ans + seen[x] * query(x, y)) % MOD
            seen[y] = seen.get(y, 0) + 1

        base = n * (n - 1) % MOD
        out.append(str(ans * pow(base, MOD - 2, MOD) % MOD))

    print("\n".join(out))

# CLAUSE: finish_program
main()
