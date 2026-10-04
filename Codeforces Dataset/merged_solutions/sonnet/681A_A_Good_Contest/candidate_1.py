import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rows = []
    pos = 1
    for _ in range(n):
        before = int(data[pos + 1])
        after = int(data[pos + 2])
        pos += 3
        rows.append((before, after))
    return rows


# --- clause: good_contest :: (rows: list[tuple[int, int]]) -> str ---
def good_contest(rows):
    for before, after in rows:
        if before >= 2400 and after > before:
            return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(good_contest(read_input()) + "\n")


if __name__ == "__main__":
    main()
