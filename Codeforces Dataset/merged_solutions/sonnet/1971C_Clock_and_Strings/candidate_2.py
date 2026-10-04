import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1], data[pos + 2], data[pos + 3]))
        pos += 4
    return cases


# --- clause: strings_cross :: (a: int, b: int, c: int, d: int) -> bool ---
def strings_cross(a, b, c, d):
    low = a if a < b else b
    high = b if a < b else a
    count = 0
    if low < c < high:
        count += 1
    if low < d < high:
        count += 1
    return count == 1

# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, c, d in read_input():
        out.append("YES" if strings_cross(a, b, c, d) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
