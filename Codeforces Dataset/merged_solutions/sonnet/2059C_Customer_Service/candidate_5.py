# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def read_case(tokens, index):
    n = tokens[index]
    index += 1
    suffixes = []
    for _ in range(n):
        last_bad = index + n
        for j in range(index + n - 1, index - 1, -1):
            if tokens[j] != 1:
                last_bad = j + 1
                break
        suffixes.append(index + n - last_bad)
        index += n
    return n, suffixes, index

def best_mex(n, suffixes):
    suffixes.sort(reverse=True)
    target = n - 1
    usable = 0
    for suffix in suffixes:
        if suffix >= target and target > 0:
            usable += 1
            target -= 1
    return usable + 1

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    index = 1
    answers = []
    for _ in range(tokens[0]):
        n, suffixes, index = read_case(tokens, index)
        answers.append(str(best_mex(n, suffixes)))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
