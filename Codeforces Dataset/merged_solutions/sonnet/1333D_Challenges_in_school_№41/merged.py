# Clause setup_environment [Confidence: 0.20]
import sys

def next_round(state, length):
    positions = []
    index = 0
    while index < length - 1:
        if state[index] == "R" and state[index + 1] == "L":
            positions.append(index + 1)
            state[index], state[index + 1] = state[index + 1], state[index]
            index += 2
        else:
            index += 1
    return positions


# Clause solve_logic [Confidence: 0.40]
def main():
    raw = sys.stdin.read().strip().split()
    n, k = int(raw[0]), int(raw[1])
    state = list(raw[2])

    timeline = []
    maximum = 0

    while True:
        positions = next_round(state, n)
        if len(positions) == 0:
            break
        timeline.append(positions)
        maximum += len(positions)

    minimum = len(timeline)
    if not minimum <= k <= maximum:
        sys.stdout.write("-1")
        return

    remaining_splits = k - minimum
    output_groups = []

    for positions in timeline:
        start = 0
        limit = len(positions) - 1
        while remaining_splits > 0 and start < limit:
            output_groups.append([positions[start]])
            start += 1
            remaining_splits -= 1
        output_groups.append(positions[start:])


# Clause finish_program [Confidence: 0.40]
    lines = []
    for group in answer:
        lines.append(str(len(group)) + " " + " ".join(map(str, group)))
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()


