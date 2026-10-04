# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    q = int(tokens[1])

    unique = []
    used = set()
    for raw in tokens[2:2 + n]:
        color = int(raw)
        if color not in used:
            used.add(color)
            unique.append(color)

    top_colors = deque(unique)
    answers = []
    for raw in tokens[2 + n:2 + n + q]:
        target = int(raw)
        skipped = []
        count = 1
        while top_colors[0] != target:
            skipped.append(top_colors.popleft())
            count += 1
        answers.append(str(count))
        chosen = top_colors.popleft()
        while skipped:
            top_colors.appendleft(skipped.pop())
        top_colors.appendleft(chosen)

    sys.stdout.write(" ".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
