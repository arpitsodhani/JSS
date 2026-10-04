# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def powers_of_k(k):
    special = {1: [1], -1: [1, -1], 0: [1, 0]}
    if k in special:
        return special[k]

    out = []
    item = 1
    while abs(item) <= 1000000000000000:
        out.append(item)
        item *= k
    return out

def count_segments(numbers, targets):
    earlier = {0: 1}
    running = 0
    result = 0

    for number in numbers:
        running = running + number
        result = result + sum(earlier.get(running - target, 0) for target in targets)
        earlier[running] = earlier.get(running, 0) + 1

    return result

def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    k = int(raw[1])
    numbers = list(map(int, raw[2:2 + n]))
    print(count_segments(numbers, powers_of_k(k)))

# CLAUSE: finish_program
main()
