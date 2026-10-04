import sys


# --- clause: read_input :: () -> str ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[1].decode()


# --- clause: shortest_walk :: (row: str) -> int ---
def shortest_walk(row):
    wanted = len(set(row))
    tally = {}
    best = len(row)
    left = 0
    right = 0
    while right < len(row):
        ch = row[right]
        tally[ch] = tally.get(ch, 0) + 1
        right += 1
        while len(tally) == wanted:
            if right - left < best:
                best = right - left
            drop = row[left]
            tally[drop] -= 1
            if tally[drop] == 0:
                del tally[drop]
            left += 1
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % shortest_walk(read_input()))


if __name__ == "__main__":
    main()
