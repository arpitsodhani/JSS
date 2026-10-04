# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    sent, got = sys.stdin.read().split()
    target_position = sum(1 if c == "+" else -1 for c in sent)
    fixed_position = sum((c == "+") - (c == "-") for c in got)
    questions = [c for c in got if c == "?"]

    ways = {fixed_position: 1}
    for _ in questions:
        next_ways = {}
        for pos, count in ways.items():
            next_ways[pos + 1] = next_ways.get(pos + 1, 0) + count
            next_ways[pos - 1] = next_ways.get(pos - 1, 0) + count
        ways = next_ways

    total = 2 ** len(questions)
    probability = ways.get(target_position, 0) / total
    sys.stdout.write(format(probability, ".12f") + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
