import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    values = data[2:2 + n]
    ropes = []
    pos = 2 + n
    for _ in range(m):
        ropes.append((data[pos], data[pos + 1]))
        pos += 2
    return values, ropes


# --- clause: total_energy :: (values: list[int], ropes: list[tuple[int, int]]) -> int ---
def total_energy(values, ropes):
    total = 0
    for x, y in ropes:
        left = values[x - 1]
        right = values[y - 1]
        total += left if left < right else right
    return total


# --- clause: main :: () -> None ---
def main():
    values, ropes = read_input()
    sys.stdout.write("%d\n" % total_energy(values, ropes))


if __name__ == "__main__":
    main()
