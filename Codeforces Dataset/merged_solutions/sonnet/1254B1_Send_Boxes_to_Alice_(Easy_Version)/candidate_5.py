# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def factor_options(total):
    options = []
    if total % 2 == 0:
        options.append(2)
        while total % 2 == 0:
            total //= 2
    divisor = 3
    while divisor * divisor <= total:
        if total % divisor == 0:
            options.append(divisor)
            while total % divisor == 0:
                total //= divisor
        divisor += 2
    if total > 1:
        options.append(total)
    return options

def cost_for_size(places, size):
    cost = 0
    groups = len(places) // size
    for group in range(groups):
        left = group * size
        right = left + size
        median = places[(left + right) // 2]
        low = left
        high = right - 1
        while low < high:
            cost += places[high] - places[low]
            low += 1
            high -= 1
    return cost

def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    places = []
    for i in range(n):
        if raw[i + 1] == b"1":
            places.append(i)

    total = len(places)
    if total == 1:
        sys.stdout.write("-1\n")
        return

    answer = min(cost_for_size(places, size) for size in factor_options(total))
    sys.stdout.write(str(answer) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
