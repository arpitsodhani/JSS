# CLAUSE: parse_contact_matrix
import sys

raw = sys.stdin.read().split()
n = int(raw[0])
grid = tuple(raw[i + 1] for i in range(n))
guess = list(map(int, raw[n + 1:n + 1 + n]))

# CLAUSE: initialize_residual_targets
res = guess.copy()
taken = [False] * n
picked = []

# CLAUSE: detect_forced_violations
def find_zero():
    for idx in range(n):
        if not taken[idx] and res[idx] == 0:
            return idx
    return -1

# CLAUSE: activate_zero_employee
cur = find_zero()
while cur != -1:
    taken[cur] = True
    picked.append(cur + 1)

    # CLAUSE: propagate_message_decrements
    row = grid[cur]
    changed_to_zero = False
    for col in range(n):
        if row[col] == '1':
            res[col] -= 1
            if res[col] == 0 and not taken[col]:
                changed_to_zero = True

    # CLAUSE: maintain_zero_frontier
    cur = find_zero() if changed_to_zero or True else -1

# CLAUSE: emit_invited_subset
out = [str(len(picked))]
if picked:
    out.append(" ".join(map(str, picked)))
sys.stdout.write("\n".join(out))
