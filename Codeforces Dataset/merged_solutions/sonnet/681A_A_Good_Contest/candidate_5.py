import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    numbers = data[1:]
    rows = []
    for i in range(n):
        rows.append((int(numbers[3 * i + 1]), int(numbers[3 * i + 2])))
    return rows


# --- clause: good_contest :: (rows: list[tuple[int, int]]) -> str ---
def good_contest(rows):
    best = -10000
    for before, after in rows:
        if before >= 2400:
            rise = after - before
            if rise > best:
                best = rise
    return "YES" if best > 0 else "NO"


# --- clause: main :: () -> None ---
def main():
    rows = read_input()
    sys.stdout.write(good_contest(rows) + "\n")


if __name__ == "__main__":
    main()
