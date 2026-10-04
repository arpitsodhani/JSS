import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    return [numbers[1 + i].decode() for i in range(n)]


# --- clause: count_layouts :: (rows: list[str]) -> int ---
def count_layouts(rows):
    mod = 1000000007
    n = len(rows)
    ways = [0] * (n + 2)
    ways[0] = 1
    step = 1
    while step < n:
        fresh = [0] * (n + 2)
        if rows[step - 1] == "f":
            level = n
            while level >= 1:
                fresh[level] = ways[level - 1]
                level -= 1
        else:
            running = 0
            level = n
            while level >= 0:
                running = (running + ways[level]) % mod
                fresh[level] = running
                level -= 1
        ways = fresh
        step += 1
    return sum(ways) % mod


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_layouts(read_input()))


if __name__ == "__main__":
    main()
