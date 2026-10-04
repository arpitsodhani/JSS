# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    rounds = []
    totals = defaultdict(int)
    pos = 1

    for _ in range(n):
        name = data[pos]
        score = int(data[pos + 1])
        pos += 2
        rounds.append((name, score))
        totals[name] += score

    target = max(totals.values())
    possible = {name for name, value in totals.items() if value == target}
    running = defaultdict(int)

    for name, score in rounds:
        running[name] += score
        if name in possible and running[name] >= target:
            sys.stdout.write(name)
            return


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


