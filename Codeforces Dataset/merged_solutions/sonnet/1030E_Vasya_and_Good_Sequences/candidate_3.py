# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def count_even_sum_segments(weights):
    prefix_parity = 0
    frequency = {0: 1, 1: 0}
    result = 0
    for weight in weights:
        prefix_parity = (prefix_parity + weight) & 1
        result += frequency[prefix_parity]
        frequency[prefix_parity] += 1
    return result

def count_unbalanced_even_segments(weights):
    n = len(weights)
    result = 0
    for start in range(n):
        total = 0
        largest = 0
        stop = start + 130
        if stop > n:
            stop = n
        index = start
        while index < stop:
            value = weights[index]
            total += value
            largest = value if value > largest else largest
            if (total & 1) == 0 and largest > total - largest:
                result += 1
            index += 1
    return result

def main():
    values = tuple(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    length = values[0]
    weights = tuple(number.bit_count() for number in values[1:length + 1])
    answer = count_even_sum_segments(weights) - count_unbalanced_even_segments(weights)
    print(answer)

# CLAUSE: finish_program
main()
