import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        pos += 2
        values = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, x, values))
    return cases


# --- clause: smallest_score :: (n: int, x: int, values: list[int]) -> int ---
def smallest_score(n, x, values):
    base = sum(abs(a - b) for a, b in zip(values, values[1:]))
    low = min(values)
    high = max(values)
    options = []
    if low > 1:
        options.append([2 * (low - 1), values[0] - 1, values[-1] - 1])
    if x > high:
        options.append([2 * (x - high), x - values[0], x - values[-1]])
    for group in options:
        best = group[0]
        for value in group:
            if value < best:
                best = value
        base += best
    return base


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, values in read_input():
        out.append(str(smallest_score(n, x, values)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
