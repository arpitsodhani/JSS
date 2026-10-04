# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_previous_free(n, blocked_positions):
    blocked = set(blocked_positions)
    previous = [-1] * n
    last = -1
    for position in range(n):
        if position not in blocked:
            last = position
        previous[position] = last
    return previous, blocked

def possible_cost(previous, n, power, unit_cost):
    position = 0
    lamps = 0
    while position < n:
        lamp_position = previous[position]
        if lamp_position == -1:
            return None
        position_after = lamp_position + power
        if position_after <= position:
            return None
        lamps += 1
        position = position_after
    return lamps * unit_cost

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    if not nums:
        return

    n, m, k = nums[:3]
    blocked_positions = nums[3:3 + m]
    costs = nums[3 + m:3 + m + k]

    previous, blocked = build_previous_free(n, blocked_positions)
    if 0 in blocked:
        print(-1)
        return

    candidates = []
    for power in range(1, k + 1):
        value = possible_cost(previous, n, power, costs[power - 1])
        if value is not None:
            candidates.append(value)

    print(min(candidates) if candidates else -1)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
