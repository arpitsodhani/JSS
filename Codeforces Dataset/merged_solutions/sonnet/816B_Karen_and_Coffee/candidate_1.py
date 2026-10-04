import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]], list[tuple[int, int]]] ---
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


# --- clause: admissible_prefix :: (k: int, recipes: list[tuple[int, int]]) -> list[int] ---
def admissible_prefix(k, recipes):
    top = 200002
    marks = [0] * (top + 2)
    for low, high in recipes:
        marks[low] += 1
        marks[high + 1] -= 1
    prefix = [0] * (top + 2)
    running = 0
    for value in range(1, top + 1):
        running += marks[value]
        prefix[value] = prefix[value - 1] + (1 if running >= k else 0)
    return prefix


# --- clause: main :: () -> None ---
def main():
    k, recipes, asked = read_input()
    prefix = admissible_prefix(k, recipes)
    out = []
    for low, high in asked:
        out.append(prefix[high] - prefix[low - 1])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
