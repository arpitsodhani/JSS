# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    n = int(sys.stdin.readline())
    total = 0
    queue = deque([1])
    while queue:
        value = queue.popleft()
        if value > n:
            continue
        total += 1
        queue.append(value * 10)
        queue.append(value * 10 + 1)


# Clause finish_program [Confidence: 0.60]
    print(answer)

main()


