import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    values = tokens[2:2 + n]
    ropes = []
    pos = 2 + n
    for _ in range(m):
        ropes.append((tokens[pos], tokens[pos + 1]))
        pos += 2
    return values, ropes


# --- clause: total_energy :: (values: list[int], ropes: list[tuple[int, int]]) -> int ---
def total_energy(values, ropes):
    total = 0
    for x, y in ropes:
        left = values[x - 1]
        high = values[y - 1]
        total += left if left < high else high
    return total


# --- clause: main :: () -> None ---
def main():
    values, ropes = read_input()
    sys.stdout.write("%d\n" % total_energy(values, ropes))


if __name__ == "__main__":
    main()
