# CLAUSE: setup_environment
import sys
from bisect import bisect_right

# CLAUSE: solve_logic
def lower_median_remainder(sorted_values, n, need, x):
    lo = 0
    hi = x - 1
    while lo < hi:
        mid = (lo + hi) // 2
        got = 0
        start = 0
        while start <= n:
            got += bisect_right(sorted_values, min(start + mid, n)) - bisect_right(sorted_values, start - 1)
            if got >= need:
                break
            start += x
        if got >= need:
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    raw = sys.stdin.buffer.read().split()
    index = 0
    tests = int(raw[index])
    index += 1
    output = []

    for _ in range(tests):
        n = int(raw[index])
        q = int(raw[index + 1])
        index += 2

        values = [int(x) for x in raw[index:index + n]]
        index += n

        queries = [int(x) for x in raw[index:index + q]]
        index += q

        values.sort()
        need = (n + 2) // 2
        cache = {}

        for x in queries:
            if x not in cache:
                cache[x] = lower_median_remainder(values, n, need, x)

        output.append(" ".join(str(cache[x]) for x in queries))

    sys.stdout.write("\n".join(output))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
