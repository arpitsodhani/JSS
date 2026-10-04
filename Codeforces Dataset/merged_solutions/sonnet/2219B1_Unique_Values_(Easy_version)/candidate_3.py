# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def cases_from_tokens(tokens):
    if not tokens:
        return []
    total = tokens[0]
    pointer = 1
    result = []
    for _ in range(total):
        if pointer == len(tokens):
            result = None
            break
        n = tokens[pointer]
        pointer += 1
        count = 2 * n + 1
        if pointer + count > len(tokens):
            result = None
            break
        result.append((n, tokens[pointer:pointer + count]))
        pointer += count
    if result is not None and pointer == len(tokens):
        return result
    n = tokens[0]
    count = 2 * n + 1
    if len(tokens) >= 1 + count and len(tokens[1:1 + count]) == count:
        return [(n, tokens[1:1 + count])]
    return []

def find_three(arr):
    first = {}
    second = {}
    for index, value in enumerate(arr, 1):
        if value not in first:
            first[value] = index
        elif value not in second:
            second[value] = index
        else:
            return first[value], second[value], index
    return None

# CLAUSE: finish_program
def main():
    tokens = [int(x) for x in sys.stdin.buffer.read().split()]
    lines = []
    for n, arr in cases_from_tokens(tokens):
        answer = find_three(arr)
        if answer is not None:
            lines.append(" ".join(str(x) for x in answer))
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
