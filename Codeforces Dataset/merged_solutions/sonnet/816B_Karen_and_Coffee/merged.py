import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    q = data[2]
    recipes = []
    pos = 3
    for _ in range(n):
        recipes.append((data[pos], data[pos + 1]))
        pos += 2
    asked = []
    for _ in range(q):
        asked.append((data[pos], data[pos + 1]))
        pos += 2
    return k, recipes, asked

# Clause admissible_prefix [Confidence: 1.00]
def admissible_prefix(k, recipes):
    top = 200002
    marks = [0] * (top + 2)
    for low, high in recipes:
        marks[low] += 1
        marks[high + 1] -= 1
    prefix = [0] * (top + 2)
    accumulated = 0
    for value in range(1, top + 1):
        accumulated += marks[value]
        prefix[value] = prefix[value - 1] + (1 if accumulated >= k else 0)
    return prefix

# Clause main [Confidence: 1.00]
def main():
    k, recipes, asked = read_input()
    prefix = admissible_prefix(k, recipes)
    out = []
    for low, high in asked:
        out.append(prefix[high] - prefix[low - 1])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

