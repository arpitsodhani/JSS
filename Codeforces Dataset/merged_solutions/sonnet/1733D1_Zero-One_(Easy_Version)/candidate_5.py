import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, bytes, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        y = int(data[pos + 2])
        a = data[pos + 3]
        b = data[pos + 4]
        pos = pos + 5
        cases.append((n, x, y, a, b))
    return cases


# --- clause: solve_case :: (n: int, x: int, y: int, a: bytes, b: bytes) -> int ---
def solve_case(n, x, y, a, b):
    spots = []
    for i in range(n):
        if a[i] != b[i]:
            spots.append(i)
    count = len(spots)
    if count % 2 == 1:
        return -1
    if count == 0:
        return 0
    if count == 2 and spots[1] - spots[0] == 1:
        return x if x <= 2 * y else 2 * y
    return (count // 2) * y


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, y, a, b in read_input():
        out.append(str(solve_case(n, x, y, a, b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
