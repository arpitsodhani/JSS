# CLAUSE: setup_environment
import sys
from bisect import bisect_left

# CLAUSE: solve_logic
def build_prefix(items):
    pref = [0]
    total = 0
    for x in items:
        total += x
        pref.append(total)
    return pref

def solve_case(n, k, a, b):
    m = n // 2
    needed_high = n - m
    sorted_pairs = sorted(zip(a, range(n)))
    sorted_values = [x for x, _ in sorted_pairs]
    index_rank = [0] * n
    for rank, pair in enumerate(sorted_pairs):
        index_rank[pair[1]] = rank

    answer = 0
    one_values = []
    best_fixed = None

    for i in range(n):
        if b[i]:
            one_values.append(a[i])
            deleted_rank = index_rank[i]
            median_pos = m
            if deleted_rank >= m:
                median_pos = m - 1
            candidate = a[i] + k + sorted_values[median_pos]
            answer = max(answer, candidate)
        else:
            if best_fixed is None or a[i] > best_fixed:
                best_fixed = a[i]

    if best_fixed is None:
        return answer

    one_values.sort()
    prefix = build_prefix(one_values)

    def can_reach(x):
        ge = n - bisect_left(sorted_values, x)
        if best_fixed >= x:
            ge -= 1
        need_more = needed_high - ge
        if need_more < 1:
            return True
        before = bisect_left(one_values, x)
        if before < need_more:
            return False
        current_sum = prefix[before] - prefix[before - need_more]
        return x * need_more - current_sum <= k

    left = 0
    right = max(a) + k + 1
    while left + 1 != right:
        middle = (left + right) >> 1
        if can_reach(middle):
            left = middle
        else:
            right = middle

    return max(answer, best_fixed + left)

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    p = 1
    out = []
    for _ in range(t):
        n = int(data[p])
        k = int(data[p + 1])
        p += 2
        a = list(map(int, data[p:p + n]))
        p += n
        b = list(map(int, data[p:p + n]))
        p += n
        out.append(str(solve_case(n, k, a, b)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
