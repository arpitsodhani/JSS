import sys


# --- clause: read_input :: () -> str ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return raw[1].decode()


# --- clause: shortest_walk :: (row: str) -> int ---
def shortest_walk(row):
    wanted = len(set(row))
    tally = {}
    have = 0
    top = len(row)
    first_side = 0
    for right in range(0, len(row)):
        ch = row[right]
        tally[ch] = tally.get(ch, 0) + 1
        if tally[ch] == 1:
            have += 1
        while have == wanted:
            if right - first_side + 1 < top:
                top = right - first_side + 1
            drop = row[first_side]
            tally[drop] -= 1
            if tally[drop] == 0:
                have -= 1
            first_side += 1
    return top


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % shortest_walk(read_input()))


if __name__ == "__main__":
    main()
