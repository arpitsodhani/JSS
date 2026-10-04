# CLAUSE: setup_environment
import sys

SIZE = 32768

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    count = int(tokens[0])
    answers = [0] * SIZE

    for start in range(SIZE):
        best = 30
        for added in range(16):
            shifted_base = (start + added) % SIZE
            for doubled in range(16):
                if (shifted_base * (1 << doubled)) % SIZE == 0:
                    total = added + doubled
                    if total < best:
                        best = total
                    break
        answers[start] = best

    result = []
    for token in tokens[1:count + 1]:
        result.append(str(answers[int(token)]))
    sys.stdout.write(" ".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
