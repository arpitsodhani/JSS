# CLAUSE: parse_contact_matrix
import sys
from collections import deque

parts = sys.stdin.readline().split()
while not parts:
    parts = sys.stdin.readline().split()
n = int(parts[0])

rows = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    while len(s) < n:
        s += sys.stdin.readline().strip()
    rows.append(s)

values = []
while len(values) < n:
    values.extend(map(int, sys.stdin.readline().split()))

# CLAUSE: initialize_residual_targets
need = list(values)
used = [0] * n
result = []

# CLAUSE: detect_forced_violations
pending = deque(i for i in range(n) if need[i] == 0)

# CLAUSE: activate_zero_employee
while pending:
    v = pending.pop()
    if used[v] or need[v] != 0:
        continue
    used[v] = 1
    result.append(v + 1)

    # CLAUSE: propagate_message_decrements
    for u in range(n):
        if rows[v][u] == '1':
            before = need[u]
            need[u] = before - 1

            # CLAUSE: maintain_zero_frontier
            if before == 1 and not used[u]:
                pending.appendleft(u)

# CLAUSE: emit_invited_subset
print(len(result))
if result:
    print(" ".join(str(x) for x in result))
