# CLAUSE: setup_environment
import sys

def main():
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    k = int(tokens[1])
    row = list(tokens[2])

# CLAUSE: solve_logic
    days = []
    total = 0

    while True:
        made = []
        pos = 0
        while pos + 1 < n:
            if row[pos] == "R" and row[pos + 1] == "L":
                made.append(pos + 1)
                row[pos], row[pos + 1] = row[pos + 1], row[pos]
                pos += 2
            else:
                pos += 1
        if not made:
            break
        days.append(made)
        total += len(made)

    if k < len(days) or k > total:
        sys.stdout.write("-1")
        return

    spare = k - len(days)
    answer = []
    for made in days:
        cut = min(spare, len(made) - 1)
        for i in range(cut):
            answer.append([made[i]])
        answer.append(made[cut:])
        spare -= cut

# CLAUSE: finish_program
    lines = []
    for group in answer:
        lines.append(str(len(group)) + " " + " ".join(map(str, group)))
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
