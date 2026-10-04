import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, bytes, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        x = int(data[pos + 1])
        y = int(data[pos + 2])
        a = data[pos + 3]
        b = data[pos + 4]
        pos += 5
        cases.append((n, x, y, a, b))
    return cases


# --- clause: solve_case :: (n: int, x: int, y: int, a: bytes, b: bytes) -> int ---
def solve_case(n, x, y, a, b):
    spots = []
    for i in range(n - 1, -1, -1):
        if a[i] != b[i]:
            spots.append(i)
    spots.reverse()
    count = len(spots)
    if count % 2 != 0:
        return -1
    if count == 0:
        return 0
    if count == 2 and spots[1] - spots[0] == 1:
        return min(x, 2 * y)
    return (count >> 1) * y


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, y, a, b in read_input():
        out.append(str(solve_case(n, x, y, a, b)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
