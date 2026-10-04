import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    stones = raw[1:1 + n]
    m = raw[1 + n]
    asked = []
    reader = 2 + n
    for _ in range(m):
        asked.append((raw[reader], raw[reader + 1], raw[reader + 2]))
        reader += 3
    return stones, asked


# --- clause: prefix_sums :: (stones: list[int]) -> tuple[list[int], list[int]] ---
def prefix_sums(stones):
    plain = [0] * (len(stones) + 1)
    for i in range(0, len(stones)):
        plain[i + 1] = plain[i] + stones[i]
    queue_order = sorted(stones)
    ranked = [0] * (len(stones) + 1)
    for i in range(0, len(queue_order)):
        ranked[i + 1] = ranked[i] + queue_order[i]
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
