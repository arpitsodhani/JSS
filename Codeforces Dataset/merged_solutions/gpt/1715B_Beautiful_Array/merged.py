# Clause derive_beauty_bounds [Confidence: 0.80]
import sys

def build(n, k, b, s):

    min_sum = b * k
    max_sum = min_sum + n * (k - 1)


# Clause validate_sum_feasibility [Confidence: 0.40]
    if min_sum > s or max_sum < s:
        return None


# Clause reserve_beauty_core [Confidence: 0.40]
    ans = [0] * n
    ans[0] = low


# Clause allocate_remainder_budget [Confidence: 1.00]
    extra = s - minimum


# Clause distribute_surplus_across_slots [Confidence: 0.40]
    i = 0
    while i < n:
        addition = rest
        if addition > k - 1:
            addition = k - 1
        answer[i] += addition
        rest -= addition
        i += 1


# Clause preserve_floor_contributions [Confidence: 0.20]
    total_beauty = sum(item // k for item in arr)
    if total_beauty != b:
        return "-1"


# Clause emit_constructed_array [Confidence: 1.00]
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    p = 1
    for _ in range(t):
        n, k, b, s = data[p:p + 4]
        p += 4
        ans = solve_case(n, k, b, s)
        if ans is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, ans)))
    sys.stdout.write("\n".join(out))

main()


