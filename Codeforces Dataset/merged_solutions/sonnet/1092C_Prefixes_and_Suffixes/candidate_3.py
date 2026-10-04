# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def classify(candidate, items, n):
    result = [""] * len(items)
    by_size = {}
    for position, text in enumerate(items):
        by_size.setdefault(len(text), []).append((position, text))

    for size in range(1, n):
        pair = by_size[size]
        first_index, first_text = pair[0]
        second_index, second_text = pair[1]
        prefix = candidate[:size]
        suffix = candidate[-size:]

        if first_text == prefix and second_text == suffix:
            result[first_index] = "P"
            result[second_index] = "S"
        elif first_text == suffix and second_text == prefix:
            result[first_index] = "S"
            result[second_index] = "P"
        else:
            return ""
    return "".join(result)

def main():
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    fragments = tokens[1:]
    large = [piece for piece in fragments if len(piece) == n - 1]
    options = (large[0] + large[1][-1], large[1] + large[0][-1])

    for option in options:
        answer = classify(option, fragments, n)
        if answer:
            print(answer)
            break

# CLAUSE: finish_program
main()
