# CLAUSE: setup_environment
import sys

WIDTH = 22
COUNT = 1 << WIDTH
INVERSE = COUNT - 1

# CLAUSE: solve_logic
def compatible_lookup(numbers):
    holder = [-1] * COUNT
    for number in numbers:
        holder[number] = number

    for shift in range(WIDTH):
        half = 1 << shift
        for block_start in range(0, COUNT, half << 1):
            lower = holder[block_start:block_start + half]
            upper_start = block_start + half
            for offset, candidate in enumerate(lower):
                position = upper_start + offset
                if holder[position] == -1:
                    holder[position] = candidate

    return holder

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    length = tokens[0]
    numbers = tokens[1:length + 1]
    lookup = compatible_lookup(numbers)
    print(" ".join(str(lookup[INVERSE ^ number]) for number in numbers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
