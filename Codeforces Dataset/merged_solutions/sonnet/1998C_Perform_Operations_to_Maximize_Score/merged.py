# Clause setup_environment [Confidence: 0.80]
import sys
from bisect import bisect_left


# Clause solve_logic [Confidence: 0.80]
def case_answer(n, k, a, b):
    lower_after_delete = n // 2
    required_at_least = n - lower_after_delete

    indexed = list(range(n))
    indexed.sort(key=lambda i: (a[i], i))
    values = [a[i] for i in indexed]
    where = [0] * n
    for r in range(n):
        where[indexed[r]] = r

    best = 0
    fixed_best = -1
    increasable = []

    for i, x in enumerate(a):
        if b[i] == 1:
            increasable.append(x)
            if where[i] < lower_after_delete:
                med = values[lower_after_delete]
            else:
                med = values[lower_after_delete - 1]
            if x + k + med > best:
                best = x + k + med
        elif x > fixed_best:
            fixed_best = x

    if fixed_best == -1:
        return best

    increasable.sort()
    sums = [0]
    for x in increasable:
        sums.append(sums[-1] + x)

    def affordable(level):
        count = n - bisect_left(values, level)
        if fixed_best >= level:
            count -= 1
        missing = required_at_least - count
        if missing <= 0:
            return True
        usable = bisect_left(increasable, level)
        if usable < missing:
            return False
        base = sums[usable] - sums[usable - missing]
        return level * missing - base <= k

    lo = 0
    hi = max(a) + k + 1
    while hi > lo + 1:
        mid = lo + (hi - lo) // 2
        if affordable(mid):
            lo = mid
        else:
            hi = mid

    score = fixed_best + lo
    if score > best:
        best = score
    return best


# Clause finish_program [Confidence: 0.80]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    at = 1
    res = []
    for _ in range(t):
        n = data[at]
        k = data[at + 1]
        at += 2
        a = data[at:at + n]
        at += n
        b = data[at:at + n]
        at += n
        res.append(str(solve_case(n, k, a, b)))
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()


