import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [(int(data[3 * i + 2]), int(data[3 * i + 3])) for i in range(n)]


# --- clause: good_contest :: (rows: list[tuple[int, int]]) -> str ---
def good_contest(rows):
    if any(before >= 2400 and after > before for before, after in rows):
        return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%s\n" % good_contest(read_input()))


if __name__ == "__main__":
    main()
