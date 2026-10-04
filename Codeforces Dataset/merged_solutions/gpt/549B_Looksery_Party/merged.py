# CLAUSE: parse_contact_matrix
import sys
from collections import deque

data = sys.stdin.read().split()
n = int(data[0])
matrix = data[1:1 + n]
guesses = list(map(int, data[1 + n:1 + 2 * n]))

# CLAUSE: initialize_residual_targets
residual = guesses[:]
invited = [False] * n
answer = []

# CLAUSE: detect_forced_violations
frontier = deque()
for i, value in enumerate(residual):
    if value == 0:
        frontier.append(i)

# CLAUSE: activate_zero_employee
while frontier:
    person = frontier.popleft()
    if invited[person] or residual[person] != 0:
        continue
    invited[person] = True
    answer.append(person + 1)

    # CLAUSE: propagate_message_decrements
    row = matrix[person]
    for target, has_contact in enumerate(row):
        if has_contact == '1':
            residual[target] -= 1

            # CLAUSE: maintain_zero_frontier
            if residual[target] == 0 and not invited[target]:
                frontier.append(target)

# CLAUSE: emit_invited_subset
print(len(answer))
if answer:
    print(*answer)
