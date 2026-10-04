import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        first = [int(token) for token in data[pos:pos + n]]
        pos += n
        second = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, first, second))
    return cases


# --- clause: best_beauty :: (n: int, first: list[int], second: list[int]) -> int ---
def best_beauty(n, first, second):
    nxt = [0] * (n + 1)
    for a, b in zip(first, second):
        nxt[a] = b
    stamp = [0] * (n + 1)
    pairs = 0
    for start in range(1, n + 1):
        if stamp[start]:
            continue
        node = start
        length = 0
        while stamp[node] == 0:
            stamp[node] = start
            node = nxt[node]
            length += 1
        pairs += length >> 1
    return 2 * pairs * (n - pairs)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, first, second in read_input():
        out.append(str(best_beauty(n, first, second)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
