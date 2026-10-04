# CLAUSE: parse_contact_matrix
import sys

items = sys.stdin.buffer.read().split()
n = int(items[0])
adjacency = [[] for _ in range(n)]
for r in range(n):
    line = items[r + 1]
    for c, ch in enumerate(line):
        if ch == 49:
            adjacency[r].append(c)
igor = [int(x) for x in items[n + 1:n + 1 + n]]

# CLAUSE: initialize_residual_targets
delta = igor[:]
seen = [False] * n
party = []

# CLAUSE: detect_forced_violations
bag = set()
for idx in range(n):
    if delta[idx] == 0:
        bag.add(idx)

# CLAUSE: activate_zero_employee
while bag:
    x = bag.pop()
    if seen[x] or delta[x] != 0:
        continue
    seen[x] = True
    party.append(x + 1)

    # CLAUSE: propagate_message_decrements
    newly_zero = []
    for y in adjacency[x]:
        delta[y] -= 1
        if delta[y] == 0:
            newly_zero.append(y)

    # CLAUSE: maintain_zero_frontier
    for y in newly_zero:
        if not seen[y]:
            bag.add(y)

# CLAUSE: emit_invited_subset
print(len(party))
if party:
    print(*party)
