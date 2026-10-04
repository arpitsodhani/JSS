import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: count_runs :: (values: list[int]) -> int ---
def count_runs(values):
    mod = 998244353
    pairs = [[0, 0], [0, 0]]
    singles = [0, 0]
    tally = 0
    for entry in values:
        p = entry & 1
        fresh = [[0, 0], [0, 0]]
        for x in (0, 1):
            for y in (0, 1):
                here = pairs[x][y]
                if here and (x + y + p) % 2 == 0:
                    tally = (tally + here) % mod
                    fresh[y][p] = (fresh[y][p] + here) % mod
        for x in (0, 1):
            if singles[x]:
                fresh[x][p] = (fresh[x][p] + singles[x]) % mod
        for x in (0, 1):
            for y in (0, 1):
                pairs[x][y] = (pairs[x][y] + fresh[x][y]) % mod
        singles[p] += 1
    return tally % mod


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_runs(read_input()))


if __name__ == "__main__":
    main()
