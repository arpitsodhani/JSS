import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    values = numbers[2:2 + n]
    ropes = []
    reader = 2 + n
    for _ in range(m):
        ropes.append((numbers[reader], numbers[reader + 1]))
        reader += 2
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
