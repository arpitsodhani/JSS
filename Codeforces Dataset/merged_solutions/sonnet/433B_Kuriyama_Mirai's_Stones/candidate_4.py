import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    stones = numbers[1:1 + n]
    m = numbers[1 + n]
    asked = []
    cursor = 2 + n
    for _ in range(m):
        asked.append((numbers[cursor], numbers[cursor + 1], numbers[cursor + 2]))
        cursor += 3
    return stones, asked


# --- clause: prefix_sums :: (stones: list[int]) -> tuple[list[int], list[int]] ---
def prefix_sums(stones):
    plain = [0]
    running = 0
    for value in stones:
        running += value
        plain.append(running)
    ranked = [0]
    running = 0
    for value in sorted(stones):
        running += value
        ranked.append(running)
    return plain, ranked


# --- clause: main :: () -> None ---
def main():
    stones, asked = read_input()
    plain, ranked = prefix_sums(stones)
    out = []
    for kind, low, high in asked:
        table = plain if kind == 1 else ranked
        out.append(table[high] - table[low - 1])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
