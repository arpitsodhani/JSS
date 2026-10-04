import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rows = []
    for i in range(n):
        rows.append((int(data[3 * i + 2]), int(data[3 * i + 3])))
    return rows


# --- clause: good_contest :: (rows: list[tuple[int, int]]) -> str ---
def good_contest(rows):
    index = 0
    total = len(rows)
    while index < total:
        before, after = rows[index]
        if after > before and before > 2399:
            return "YES"
        index += 1
    return "NO"


# --- clause: main :: () -> None ---
def main():
    verdict = good_contest(read_input())
    sys.stdout.write(verdict + "\n")


if __name__ == "__main__":
    main()
