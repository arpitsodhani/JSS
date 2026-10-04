import sys

def build(n, k, b, s):
    # CLAUSE: derive_beauty_bounds
    min_sum = b * k
    max_sum = min_sum + n * (k - 1)

    # CLAUSE: validate_sum_feasibility
    if min_sum > s or max_sum < s:
        return None

    # CLAUSE: reserve_beauty_core
    answer = []
    answer.append(min_sum)
    answer.extend([0] * (n - 1))

    # CLAUSE: allocate_remainder_budget
    rest = s - min_sum

    # CLAUSE: distribute_surplus_across_slots
    i = 0
    while i < n:
        addition = rest
        if addition > k - 1:
            addition = k - 1
        answer[i] += addition
        rest -= addition
        i += 1

    # CLAUSE: preserve_floor_contributions
    unchanged = True
    for i in range(1, n):
        if answer[i] >= k:
            unchanged = False
            break
    if not unchanged or answer[0] // k != b:
        return None

    # CLAUSE: emit_constructed_array
    return answer

def main():
    data = sys.stdin.buffer.read().split()
    cases = int(data[0])
    cursor = 1
    output = []
    for _ in range(cases):
        n, k, b, s = map(int, data[cursor:cursor + 4])
        cursor += 4
        ans = build(n, k, b, s)
        output.append("-1" if ans is None else " ".join(map(str, ans)))
    sys.stdout.write("\n".join(output))

main()
