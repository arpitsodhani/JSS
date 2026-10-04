# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def main():
    data = tuple(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    sequence = data[2:2 + n]

    targets = []
    if k == 1:
        targets.append(1)
    elif k == -1:
        targets.extend((1, -1))
    elif k == 0:
        targets.extend((1, 0))
    else:
        current = 1
        while abs(current) <= 10 ** 15:
            targets.append(current)
            current *= k

    frequencies = Counter()
    frequencies[0] = 1
    current_sum = 0
    answer = 0

    for element in sequence:
        current_sum += element
        for candidate in targets:
            answer += frequencies[current_sum - candidate]
        frequencies[current_sum] += 1

    sys.stdout.write(str(answer) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
