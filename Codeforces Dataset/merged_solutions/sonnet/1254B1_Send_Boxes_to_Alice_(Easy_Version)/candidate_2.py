# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def group_cost(positions, size):
    total = 0
    count = len(positions)
    for left in range(0, count, size):
        median = positions[left + size // 2]
        for right in range(left, left + size):
            total += abs(positions[right] - median)
    return total

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    positions = []
    for i in range(n):
        if int(data[i + 1]) == 1:
            positions.append(i)

    total_ones = len(positions)
    if total_ones == 1:
        print(-1)
        return

    factors = []
    x = total_ones
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        factors.append(x)

    answer = 10 ** 18
    for factor in factors:
        answer = min(answer, group_cost(positions, factor))
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
