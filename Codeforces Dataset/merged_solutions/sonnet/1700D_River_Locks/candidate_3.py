# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def read_numbers():
    return map(int, sys.stdin.buffer.read().split())

def main():
    numbers = iter(read_numbers())
    n = next(numbers)

    prefix_sum = 0
    required_time = 0
    for position in range(1, n + 1):
        prefix_sum += next(numbers)
        candidate = (prefix_sum - 1) // position + 1
        required_time = max(required_time, candidate)

    total_volume = prefix_sum
    q = next(numbers)

    answers = []
    for _ in range(q):
        seconds = next(numbers)
        answer = -1 if seconds < required_time else (total_volume - 1) // seconds + 1
        answers.append(str(answer))

    print("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
