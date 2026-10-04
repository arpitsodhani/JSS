# CLAUSE: setup_environment
import sys

def emit(groups):
    pieces = []
    for group in groups:
        pieces.append(str(len(group)))
        pieces.extend(str(x) for x in group)
        pieces.append("\n")
    if pieces:
        pieces.pop()
    return " ".join(pieces).replace(" \n ", "\n").replace(" \n", "\n")

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    s = bytearray(data[2])

    all_steps = []
    total_swaps = 0

    while True:
        indices = []
        i = 0
        while i < n - 1:
            if s[i] == 82 and s[i + 1] == 76:
                indices.append(i + 1)
                s[i], s[i + 1] = s[i + 1], s[i]
                i += 2
            else:
                i += 1
        if not indices:
            break
        all_steps.append(indices)
        total_swaps += len(indices)

    base_seconds = len(all_steps)
    if k < base_seconds or total_swaps < k:
        sys.stdout.write("-1")
        return

    split_budget = k - base_seconds
    schedule = []

    for indices in all_steps:
        single = len(indices) - 1
        take = single if single < split_budget else split_budget
        if take:
            schedule.extend([indices[j]] for j in range(take))
        schedule.append(indices[take:])
        split_budget -= take

# CLAUSE: finish_program
    sys.stdout.write(emit(schedule))

if __name__ == "__main__":
    main()
