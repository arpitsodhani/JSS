# Clause setup_environment [Confidence: 0.20]
import sys

def build_counter(values, size):
    counter = [0] * (size + 1)
    for value in values:
        counter[value] += 1
    return counter


# Clause solve_logic [Confidence: 0.40]
def can_make(divisor, values, k):
    start = 0
    size = len(values)
    multiple = divisor
    largest = values[-1]
    while multiple <= largest:
        right = multiple + k
        cap = multiple + divisor - 1
        if right > cap:
            right = cap
        left_index = bisect_left(values, multiple, start)
        right_index = bisect_right(values, right, left_index)
        if left_index != start:
            return False
        start = right_index
        if start == size:
            return True
        multiple += divisor
    return start == size

def main():
    n, k, values = load()
    values.sort()
    limit = values[0]
    for divisor in range(limit, 0, -1):
        if can_make(divisor, values, k):
            sys.stdout.write(str(divisor))
            return


# Clause finish_program [Confidence: 0.40]
main()


