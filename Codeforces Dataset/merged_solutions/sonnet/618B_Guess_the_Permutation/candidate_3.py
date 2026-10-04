# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def row_maximums(numbers, n):
    answer = []
    start = 1
    for i in range(n):
        answer.append(max(numbers[start:start + n]))
        start += n
    return answer

def main():
    numbers = [int(x) for x in sys.stdin.buffer.read().split()]
    n = numbers[0]
    answer = row_maximums(numbers, n)

    present = set(answer)
    missing = next(x for x in range(1, n + 1) if x not in present)

    seen = set()
    for i, value in enumerate(answer):
        if value in seen:
            answer[i] = missing
            break
        seen.add(value)

    print(*answer)

# CLAUSE: finish_program
main()
