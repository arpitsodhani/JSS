# CLAUSE: setup_environment
import sys

def main():
    values = sys.stdin.read().strip().split()
    n = int(values[0])
    pos = int(values[1])
    l = int(values[2])
    r = int(values[3])

# CLAUSE: solve_logic
    actions = 0
    targets = []
    if l != 1:
        targets.append(l)
        actions += 1
    if r != n:
        targets.append(r)
        actions += 1

    if not targets:
        result = 0
    elif len(targets) == 1:
        result = abs(pos - targets[0]) + actions
    else:
        span = targets[1] - targets[0]
        result = min(abs(pos - targets[0]), abs(pos - targets[1])) + span + actions

# CLAUSE: finish_program
    sys.stdout.write(f"{result}\n")

main()
