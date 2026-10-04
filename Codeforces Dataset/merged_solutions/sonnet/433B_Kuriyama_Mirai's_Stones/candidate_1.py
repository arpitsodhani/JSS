import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    stones = data[1:1 + n]
    m = data[1 + n]
    asked = []
    pos = 2 + n
    for _ in range(m):
        asked.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return stones, asked


# --- clause: prefix_sums :: (stones: list[int]) -> tuple[list[int], list[int]] ---
def prefix_sums(stones):
    plain = [0] * (len(stones) + 1)
    for i in range(len(stones)):
        plain[i + 1] = plain[i] + stones[i]
    order = sorted(stones)
    ranked = [0] * (len(stones) + 1)
    for i in range(len(order)):
        ranked[i + 1] = ranked[i] + order[i]
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
