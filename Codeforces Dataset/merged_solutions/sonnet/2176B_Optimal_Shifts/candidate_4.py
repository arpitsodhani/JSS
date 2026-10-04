import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    return [numbers[2 + 2 * i].decode() for i in range(t)]


# --- clause: widest_gap :: (s: str) -> int ---
def widest_gap(s):
    n = len(s)
    first = -1
    last = -1
    widest = 0
    for i in range(n):
        if s[i] != "1":
            continue
        if first < 0:
            first = i
        elif i - last > widest:
            widest = i - last
        last = i
    wrap = first + n - last
    if wrap > widest:
        widest = wrap
    return widest - 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(widest_gap(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
