# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    q = int(tokens[0])
    at = 1
    answers = [None] * q
    for case in range(q):
        n = int(tokens[at])
        k = int(tokens[at + 1])
        at += 2
        base_sum = 0
        scored = [0] * n
        for offset in range(n):
            val = int(tokens[at + offset])
            base_sum += val
            scored[offset] = val + offset + 1
        at += n
        scored.sort()
        avoided = 0
        for value in scored[n - k:]:
            avoided += value
        answers[case] = str(base_sum + k * n - k * (k - 1) // 2 - avoided)
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
