# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def answer_for(a):
    pairs = []
    for index, value in enumerate(a):
        pairs.append((value, index))
    pairs.sort()
    best = 0
    length = 0
    previous_index = -1
    for value, index in pairs:
        if previous_index < index:
            length += 1
        else:
            length = 1
        previous_index = index
        if length > best:
            best = length
    return len(a) - best

def main():
    tokens = sys.stdin.buffer.read().split()
    cases = int(tokens[0])
    at = 1
    result = []
    for _ in range(cases):
        n = int(tokens[at])
        at += 1
        arr = list(map(int, tokens[at:at + n]))
        at += n
        result.append(str(answer_for(arr)))
    print("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
