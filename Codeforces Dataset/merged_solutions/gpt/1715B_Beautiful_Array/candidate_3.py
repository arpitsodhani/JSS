import sys

def make_array(n, k, b, s):
    # CLAUSE: derive_beauty_bounds
    base_sum = b * k
    spare_capacity = n * (k - 1)
    upper_sum = base_sum + spare_capacity

    # CLAUSE: validate_sum_feasibility
    if not (base_sum <= s <= upper_sum):
        return None

    # CLAUSE: reserve_beauty_core
    values = [0 for _ in range(n)]
    values[-1] = base_sum

    # CLAUSE: allocate_remainder_budget
    remaining = s - base_sum

    # CLAUSE: distribute_surplus_across_slots
    for pos in range(n - 1, -1, -1):
        take = min(k - 1, remaining)
        values[pos] = values[pos] + take
        remaining = remaining - take

    # CLAUSE: preserve_floor_contributions
    beauty = 0
    for value in values:
        beauty += value // k
    if beauty != b:
        return None

    # CLAUSE: emit_constructed_array
    return values

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    tests = next(it)
    answers = []
    for _ in range(tests):
        n = next(it)
        k = next(it)
        b = next(it)
        s = next(it)
        built = make_array(n, k, b, s)
        if built is None:
            answers.append("-1")
        else:
            answers.append(" ".join(str(x) for x in built))
    sys.stdout.write("\n".join(answers))

main()
