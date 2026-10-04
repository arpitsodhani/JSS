# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def read_rounds():
    raw = sys.stdin.buffer.read().split()
    total_rounds = int(raw[0])
    return [(raw[i].decode(), int(raw[i + 1])) for i in range(1, 2 * total_rounds + 1, 2)]

def main():
    rounds = read_rounds()
    totals = Counter()

    for item in rounds:
        totals[item[0]] += item[1]

    best_score = totals.most_common(1)[0][1]
    finalists = set(filter(lambda name: totals[name] == best_score, totals))

    partial = Counter()
    for item in rounds:
        player, change = item
        partial[player] += change
        if player in finalists and partial[player] >= best_score:
            sys.stdout.write(player)
            break

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
