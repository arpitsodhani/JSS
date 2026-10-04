# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def pick_weight(weight, occupied):
    lower = weight - 1
    if lower > 0 and lower not in occupied:
        return lower
    if weight not in occupied:
        return weight
    upper = weight + 1
    if upper not in occupied:
        return upper
    return 0

def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    count = data[0]
    weights = sorted(data[1:count + 1])
    occupied = set()
    total = 0
    for weight in weights:
        assigned = pick_weight(weight, occupied)
        if assigned:
            occupied.add(assigned)
            total += 1
    print(total)

# CLAUSE: finish_program
main()
