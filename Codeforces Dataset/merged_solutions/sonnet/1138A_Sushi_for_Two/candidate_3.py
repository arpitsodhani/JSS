# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def longest_balanced_segment(types):
    best = 0
    previous_run = 0
    current_run = 1
    for index in range(1, len(types)):
        if types[index] == types[index - 1]:
            current_run += 1
        else:
            candidate = 2 * min(previous_run, current_run)
            if candidate > best:
                best = candidate
            previous_run = current_run
            current_run = 1
    candidate = 2 * min(previous_run, current_run)
    if candidate > best:
        best = candidate
    return best

def main():
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    types = [int(x) for x in tokens[1:n + 1]]
    print(longest_balanced_segment(types))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
