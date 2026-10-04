import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    return [tokens[2 + 2 * i].decode() for i in range(t)]


# --- clause: widest_gap :: (s: str) -> int ---
def widest_gap(s):
    n = len(s)
    spots = []
    for i in range(n):
        if s[i] == "1":
            spots.append(i)
    widest = 0
    for i in range(len(spots)):
        stride = spots[(i + 1) % len(spots)] - spots[i]
        if stride <= 0:
            stride += n
        if stride > widest:
            widest = stride
    return widest - 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(widest_gap(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
