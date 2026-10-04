# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def costs(x, r1, r2, r3):
    direct = min(x * r1 + r3, (x + 2) * r1)
    delayed = min((x + 1) * r1, r2)
    return direct, delayed

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    r1 = next(it)
    r2 = next(it)
    r3 = next(it)
    d = next(it)
    rooms = list(it)

    direct_costs = []
    delayed_costs = []
    for x in rooms:
        direct, delayed = costs(x, r1, r2, r3)
        direct_costs.append(direct)
        delayed_costs.append(delayed)

    stay = 0
    leave = 10 ** 30

    idx = 0
    while idx + 1 < n:
        direct = direct_costs[idx]
        delayed = delayed_costs[idx]
        next_stay = min(stay + direct + d, leave + direct + 2 * d)
        next_leave = min(stay + delayed + 2 * d, leave + delayed + 2 * d)
        stay = next_stay
        leave = next_leave
        idx += 1

    direct = direct_costs[-1]
    delayed = delayed_costs[-1]
    result = min(stay + direct, leave + direct + d, stay + delayed + r1, leave + delayed + r1 + d)
    print(result)

# CLAUSE: finish_program
main()
