# CLAUSE: parse_contact_matrix
import sys

tokens = sys.stdin.buffer.read().split()
n = int(tokens[0])
contacts = []
for i in range(n):
    row = tokens[1 + i].decode()
    contacts.append([j for j, bit in enumerate(row) if bit == '1'])
predicted = [int(x) for x in tokens[1 + n:1 + 2 * n]]

# CLAUSE: initialize_residual_targets
remaining = predicted[:]
chosen = [False for _ in range(n)]
invited_order = []

# CLAUSE: detect_forced_violations
zeros = [i for i in range(n) if remaining[i] == 0]

# CLAUSE: activate_zero_employee
while zeros:
    employee = zeros.pop()
    if chosen[employee] or remaining[employee] != 0:
        continue
    chosen[employee] = True
    invited_order.append(employee + 1)

    # CLAUSE: propagate_message_decrements
    for receiver in contacts[employee]:
        remaining[receiver] -= 1

        # CLAUSE: maintain_zero_frontier
        if remaining[receiver] == 0 and not chosen[receiver]:
            zeros.append(receiver)

# CLAUSE: emit_invited_subset
sys.stdout.write(str(len(invited_order)) + "\n")
if invited_order:
    sys.stdout.write(" ".join(map(str, invited_order)) + "\n")
