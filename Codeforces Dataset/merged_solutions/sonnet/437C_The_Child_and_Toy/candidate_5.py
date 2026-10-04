import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    values = raw[2:2 + n]
    ropes = []
    offset = 2 + n
    for _ in range(m):
        ropes.append((raw[offset], raw[offset + 1]))
        offset += 2
    return values, ropes


# --- clause: total_energy :: (values: list[int], ropes: list[tuple[int, int]]) -> int ---
def total_energy(values, ropes):
    total = 0
    for x, y in ropes:
        left = values[x - 1]
        second_side = values[y - 1]
        total += left if left < second_side else second_side
    return total


# --- clause: main :: () -> None ---
def main():
    values, ropes = read_input()
    sys.stdout.write("%d\n" % total_energy(values, ropes))


if __name__ == "__main__":
    main()
