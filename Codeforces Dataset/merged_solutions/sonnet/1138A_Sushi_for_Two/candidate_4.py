# CLAUSE: setup_environment
import sys
from itertools import groupby

# CLAUSE: solve_logic
def main():
    values = sys.stdin.buffer.read().split()
    n = int(values[0])
    sequence = [int(x) for x in values[1:n + 1]]
    lengths = [sum(1 for _ in group) for _, group in groupby(sequence)]
    answer = max((2 * min(lengths[i], lengths[i - 1]) for i in range(1, len(lengths))), default=0)
    sys.stdout.write(f"{answer}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
