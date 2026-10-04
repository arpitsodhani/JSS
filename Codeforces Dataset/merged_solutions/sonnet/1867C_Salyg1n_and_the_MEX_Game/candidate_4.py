# CLAUSE: setup_environment
import sys

def next_missing(used, start):
    while used[start]:
        start += 1
    return start

# CLAUSE: solve_logic
read = sys.stdin.readline
case_count = int(read())
for _ in range(case_count):
    n = int(read())
    values = list(map(int, read().split()))
    limit = n * 2 + 5
    used = [False] * limit
    extra = set()
    for value in values:
        if value < limit:
            used[value] = True
        else:
            extra.add(value)
    current = next_missing(used, 0)
    while True:
        print(current, flush=True)
        if current < limit:
            used[current] = True
        else:
            extra.add(current)
        removed = int(read())
        if removed == -1:
            break
        if removed < limit:
            used[removed] = False
            if removed < current:
                current = removed
        else:
            extra.discard(removed)
        current = next_missing(used, current)

# CLAUSE: finish_program
