# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.60]
def run():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    values = [int(x) for x in tokens[1:]]
    if len(values) != n:
        return

    by_residue = [[], [], []]
    for pos, value in enumerate(values, 1):
        by_residue[value % 3].append((value, pos))

    for group in by_residue:
        group.sort()

    next_item = [0, 0, 0]
    result = [0] * n
    current = 0

    for step in range(n):
        residue = step % 3
        pointer = next_item[residue]

        if pointer >= len(by_residue[residue]):
            sys.stdout.write("Impossible\n")
            return

        value, index = by_residue[residue][pointer]
        if value > current:
            sys.stdout.write("Impossible\n")
            return

        result[step] = index
        next_item[residue] = pointer + 1
        current = value + 1

    sys.stdout.write("Possible\n")
    sys.stdout.write(" ".join(str(x) for x in result) + "\n")


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


