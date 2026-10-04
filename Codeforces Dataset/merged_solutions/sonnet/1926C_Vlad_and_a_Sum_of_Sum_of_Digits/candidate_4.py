# CLAUSE: setup_environment
import sys

def build_answers(limit):
    sums = [0] * (limit + 1)
    running = 0
    for n in range(1, limit + 1):
        x = n
        while x:
            running += x % 10
            x //= 10
        sums[n] = running
    return sums

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    tests = int(tokens[0])
    requested = [int(x) for x in tokens[1:tests + 1]]
    answers = build_answers(max(requested) if requested else 0)
    sys.stdout.write("\n".join(map(lambda n: str(answers[n]), requested)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
