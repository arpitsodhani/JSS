# CLAUSE: setup_environment
import sys
from bisect import bisect_left

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    q = raw[0]
    i = 1
    ans = [""] * q
    for tc in range(q):
        n = raw[i]
        k = raw[i + 1]
        i += 2
        a = raw[i:i + n]
        i += n
        b = raw[i:i + n]
        i += n
        ans[tc] = str(case_answer(n, k, a, b))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
