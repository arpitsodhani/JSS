# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def make_numbers(limit):
    values = [1]
    index = 0
    while index < len(values):
        value = values[index]
        index += 1
        next_zero = value * 10
        next_one = next_zero + 1
        if next_zero <= limit:
            values.append(next_zero)
        if next_one <= limit:
            values.append(next_one)
    return values

def main():
    n = int(sys.stdin.readline())
    answer = len(make_numbers(n))

# CLAUSE: finish_program
    print(answer)

main()
