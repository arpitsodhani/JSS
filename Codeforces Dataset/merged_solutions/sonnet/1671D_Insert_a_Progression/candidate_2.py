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
        values = list(map(int, data[pos:pos + n]))
        pos += n
        cases.append((n, x, values))
    return cases


# --- clause: smallest_score :: (n: int, x: int, values: list[int]) -> int ---
def smallest_score(n, x, values):
    base = 0
    for i in range(1, n):
        base += abs(values[i] - values[i - 1])
    low = values[0]
    high = values[0]
    for value in values:
        if value < low:
            low = value
        if value > high:
            high = value
    if low > 1:
        inside = 2 * (low - 1)
        front = values[0] - 1
        back = values[n - 1] - 1
        base += min(inside, front, back)
    if x > high:
        inside = 2 * (x - high)
        front = x - values[0]
        back = x - values[n - 1]
        base += min(inside, front, back)
    return base


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, values in read_input():
        out.append(str(smallest_score(n, x, values)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
