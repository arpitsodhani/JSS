# CLAUSE: setup_environment
import sys

data_in = sys.stdin.readline

# CLAUSE: solve_logic
tests = int(data_in())
for _ in range(tests):
    size = int(data_in())
    present = set(int(v) for v in data_in().split())
    candidate = 0
    while candidate in present:
        candidate += 1
    active = True
    while active:
        sys.stdout.write(str(candidate) + "\n")
        sys.stdout.flush()
        present.add(candidate)
        removed = int(data_in())
        if removed == -1:
            active = False
        else:
            present.discard(removed)
            if removed < candidate:
                candidate = removed
            while candidate in present:
                candidate += 1

# CLAUSE: finish_program
