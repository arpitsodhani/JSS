# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(tokens)
    answer = 0
    for start, gap in zip(tokens, tokens):
        delta = answer - start
        if delta < 0:
            answer = start
        else:
            answer = start + (delta // gap + 1) * gap
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
