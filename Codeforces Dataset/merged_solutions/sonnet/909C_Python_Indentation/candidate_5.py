import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    return [raw[1 + i].decode() for i in range(n)]


# --- clause: count_layouts :: (rows: list[str]) -> int ---
def count_layouts(rows):
    mod = 1000000007
    n = len(rows)
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n):
        fresh = [0] * (n + 1)
        if rows[i - 1] == "f":
            for level in range(1, n + 1):
                fresh[level] = ways[level - 1]
        else:
            running = 0
            for level in range(n, -1, -1):
                running = (running + ways[level]) % mod
                fresh[level] = running
        ways = fresh
    tally = 0
    for number in ways:
        tally = (tally + number) % mod
    return tally


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_layouts(read_input()))


if __name__ == "__main__":
    main()
