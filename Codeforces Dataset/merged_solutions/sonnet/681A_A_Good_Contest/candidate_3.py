import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rows = []
    pos = 1
    while len(rows) < n:
        rows.append((int(data[pos + 1]), int(data[pos + 2])))
        pos += 3
    return rows


# --- clause: good_contest :: (rows: list[tuple[int, int]]) -> str ---
def good_contest(rows):
    reds = [pair for pair in rows if pair[0] >= 2400]
    gained = 0
    for before, after in reds:
        if after - before > 0:
            gained += 1
    if gained:
        return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    print(good_contest(read_input()))


if __name__ == "__main__":
    main()
