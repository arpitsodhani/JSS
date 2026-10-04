# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
tokens = sys.stdin.buffer.read().split()
text = tokens[0].decode()
size = len(text)
queries = int(tokens[1])
palindrome = [[0] * size for _ in range(size)]

for center in range(size):
    left = right = center
    while left >= 0 and right < size and text[left] == text[right]:
        palindrome[left][right] = 1
        left -= 1
        right += 1
    left = center
    right = center + 1
    while left >= 0 and right < size and text[left] == text[right]:
        palindrome[left][right] = 1
        left -= 1
        right += 1

total = [[0] * size for _ in range(size)]
for right in range(size):
    running = 0
    for left in range(right, -1, -1):
        running += palindrome[left][right]
        total[left][right] = running
        if right > 0:
            total[left][right] += total[left][right - 1]

answers = []
at = 2
for _ in range(queries):
    left = int(tokens[at]) - 1
    right = int(tokens[at + 1]) - 1
    at += 2
    answers.append(str(total[left][right]))


# Clause finish_program [Confidence: 0.80]
sys.stdout.write("\n".join(out))


