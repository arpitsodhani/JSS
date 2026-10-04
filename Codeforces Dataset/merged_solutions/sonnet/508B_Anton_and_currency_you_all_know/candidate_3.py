# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def find_swap_position(number):
    tail = number[-1]
    fallback = None
    for position, character in enumerate(number[:-1]):
        if character in "02468":
            fallback = position
            if character < tail:
                return position
    return fallback

def main():
    number = sys.stdin.readline().strip()
    position = find_swap_position(number)

    if position is None:
        print(-1)
        return

    answer = number[:position] + number[-1] + number[position + 1:-1] + number[position]
    print(answer)

# CLAUSE: finish_program
main()
