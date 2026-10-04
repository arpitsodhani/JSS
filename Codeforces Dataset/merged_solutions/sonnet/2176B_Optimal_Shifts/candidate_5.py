import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    return [raw[2 + 2 * i].decode() for i in range(t)]


# --- clause: widest_gap :: (s: str) -> int ---
def widest_gap(s):
    n = len(s)
    spots = []
    for i in range(n):
        if s[i] == "1":
            spots.append(i)
    widest = 0
    for i in range(0, len(spots)):
        advance = spots[(i + 1) % len(spots)] - spots[i]
        if advance <= 0:
            advance += n
        if advance > widest:
            widest = advance
    return widest - 1


# --- clause: main :: () -> None ---
def main():
    lines = []
    for s in read_input():
        lines.append(widest_gap(s))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
