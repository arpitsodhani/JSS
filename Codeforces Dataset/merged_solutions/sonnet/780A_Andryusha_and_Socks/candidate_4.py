# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    seen = [False] * (n + 1)
    on_table = 0
    answer = 0
    index = 1
    while index < len(tokens):
        sock = int(tokens[index])
        if seen[sock]:
            on_table -= 1
        else:
            seen[sock] = True
            on_table += 1
            if on_table > answer:
                answer = on_table
        index += 1

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
