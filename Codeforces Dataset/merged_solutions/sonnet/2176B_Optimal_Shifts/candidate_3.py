import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    return [fields[2 + 2 * i].decode() for i in range(t)]


# --- clause: widest_gap :: (s: str) -> int ---
def widest_gap(s):
    n = len(s)
    spots = []
    for i in range(n):
        if s[i] == "1":
            spots.append(i)
    widest = 0
    for i in range(len(spots)):
        delta = spots[(i + 1) % len(spots)] - spots[i]
        if delta <= 0:
            delta += n
        if delta > widest:
            widest = delta
    return widest - 1


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for s in read_input():
        pieces.append(widest_gap(s))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
