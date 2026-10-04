import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]], list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    q = numbers[2]
    recipes = []
    reader = 3
    for _ in range(n):
        recipes.append((numbers[reader], numbers[reader + 1]))
        reader += 2
    asked = []
    for _ in range(q):
        asked.append((numbers[reader], numbers[reader + 1]))
        reader += 2
    return k, recipes, asked


# --- clause: admissible_prefix :: (k: int, recipes: list[tuple[int, int]]) -> list[int] ---
def admissible_prefix(k, recipes):
    top = 200002
    depth = [0] * (top + 2)
    for low, high in recipes:
        depth[low] += 1
        depth[high + 1] -= 1
    running = 0
    prefix = [0] * (top + 2)
    for value in range(top + 1):
        running += depth[value]
        prefix[value] = (prefix[value - 1] if value else 0) + (1 if running >= k and value >= 1 else 0)
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
