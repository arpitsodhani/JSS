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
    span = set()
    position = a % 12 + 1
    while position != b:
        span.add(position)
        position = position % 12 + 1
    inside = (c in span) + (d in span)
    return inside == 1

# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, c, d in read_input():
        out.append("YES" if strings_cross(a, b, c, d) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
