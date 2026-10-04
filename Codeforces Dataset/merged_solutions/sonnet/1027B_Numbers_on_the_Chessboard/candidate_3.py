import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    q = fields[1]
    asked = []
    for i in range(q):
        asked.append((fields[2 + 2 * i], fields[3 + 2 * i]))
    return n, asked


# --- clause: cell_value :: (n: int, x: int, y: int) -> int ---
def cell_value(n, x, y):
    place = (x - 1) * n + y - 1
    half = (n * n + 1) // 2
    if (x + y) % 2 == 0:
        return place // 2 + 1
    return half + place // 2 + 1


# --- clause: main :: () -> None ---
def main():
    n, asked = read_input()
    collected = []
    for x, y in asked:
        collected.append(cell_value(n, x, y))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()
