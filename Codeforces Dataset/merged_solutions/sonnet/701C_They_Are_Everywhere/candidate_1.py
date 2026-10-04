import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()


# --- clause: shortest_walk :: (row: str) -> int ---
def shortest_walk(row):
    wanted = len(set(row))
    tally = {}
    have = 0
    best = len(row)
    left = 0
    for right in range(len(row)):
        ch = row[right]
        tally[ch] = tally.get(ch, 0) + 1
        if tally[ch] == 1:
            have += 1
        while have == wanted:
            if right - left + 1 < best:
                best = right - left + 1
            drop = row[left]
            tally[drop] -= 1
            if tally[drop] == 0:
                have -= 1
            left += 1
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % shortest_walk(read_input()))


if __name__ == "__main__":
    main()
