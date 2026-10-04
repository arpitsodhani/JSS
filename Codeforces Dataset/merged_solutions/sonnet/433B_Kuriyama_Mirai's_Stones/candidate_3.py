import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    stones = fields[1:1 + n]
    m = fields[1 + n]
    asked = []
    offset = 2 + n
    for _ in range(m):
        asked.append((fields[offset], fields[offset + 1], fields[offset + 2]))
        offset += 3
    return stones, asked


# --- clause: prefix_sums :: (stones: list[int]) -> tuple[list[int], list[int]] ---
def prefix_sums(stones):
    plain = [0] * (len(stones) + 1)
    for i in range(len(stones)):
        plain[i + 1] = plain[i] + stones[i]
    arranged = sorted(stones)
    ranked = [0] * (len(stones) + 1)
    for i in range(len(arranged)):
        ranked[i + 1] = ranked[i] + arranged[i]
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
