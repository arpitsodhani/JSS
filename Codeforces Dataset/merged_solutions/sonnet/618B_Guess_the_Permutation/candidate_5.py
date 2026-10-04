# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    answer = [0] * n

    for index in range(n):
        offset = 1 + index * n
        for column in range(n):
            value = raw[offset + column]
            if value > answer[index]:
                answer[index] = value

    counts = [0] * (n + 1)
    for value in answer:
        counts[value] += 1

    missing = 1
    for candidate in range(1, n + 1):
        if counts[candidate] == 0:
            missing = candidate
            break

    for index in range(n - 1, -1, -1):
        value = answer[index]
        if counts[value] > 1:
            answer[index] = missing
            break

    sys.stdout.write(" ".join(map(str, answer)))

# CLAUSE: finish_program
main()
