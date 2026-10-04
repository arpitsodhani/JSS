import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    values = fields[2:2 + n]
    ropes = []
    cursor = 2 + n
    for _ in range(m):
        ropes.append((fields[cursor], fields[cursor + 1]))
        cursor += 2
    return values, ropes


# --- clause: total_energy :: (values: list[int], ropes: list[tuple[int, int]]) -> int ---
def total_energy(values, ropes):
    total = 0
    for x, y in ropes:
        left = values[x - 1]
        finish = values[y - 1]
        total += left if left < finish else finish
    return total


# --- clause: main :: () -> None ---
def main():
    values, ropes = read_input()
    sys.stdout.write("%d\n" % total_energy(values, ropes))


if __name__ == "__main__":
    main()
