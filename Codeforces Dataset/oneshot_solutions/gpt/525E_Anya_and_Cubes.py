import sys
from collections import defaultdict

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, k, S = data[0], data[1], data[2]
    a = data[3:3 + n]

    fact = [1] * 19
    for i in range(1, 19):
        fact[i] = fact[i - 1] * i

    vals = []
    for x in a:
        fx = fact[x] if x <= 18 else None
        if fx is not None and fx > S:
            fx = None
        vals.append((x, fx))

    mid = n // 2
    left = vals[:mid]
    right = vals[mid:]

    counts = [defaultdict(int) for _ in range(k + 1)]

    def enum_left(i, used, total):
        if total > S or used > k:
            return
        if i == len(left):
            counts[used][total] += 1
            return
        x, fx = left[i]
        enum_left(i + 1, used, total)
        enum_left(i + 1, used, total + x)
        if fx is not None:
            enum_left(i + 1, used + 1, total + fx)

    ans = 0

    def enum_right(i, used, total):
        nonlocal ans
        if total > S or used > k:
            return
        if i == len(right):
            need = S - total
            for c in range(k - used + 1):
                ans += counts[c].get(need, 0)
            return
        x, fx = right[i]
        enum_right(i + 1, used, total)
        enum_right(i + 1, used, total + x)
        if fx is not None:
            enum_right(i + 1, used + 1, total + fx)

    enum_left(0, 0, 0)
    enum_right(0, 0, 0)

    print(ans)

if __name__ == "__main__":
    main()
