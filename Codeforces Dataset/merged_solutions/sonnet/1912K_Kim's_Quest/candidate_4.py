import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: count_runs :: (values: list[int]) -> int ---
def count_runs(values):
    mod = 998244353
    pairs = {}
    singles = {0: 0, 1: 0}
    total = 0
    for value in values:
        p = value % 2
        fresh = {}
        for key in pairs:
            x, y = key
            if (x + y + p) % 2:
                continue
            here = pairs[key]
            total = (total + here) % mod
            spot = (y, p)
            fresh[spot] = (fresh.get(spot, 0) + here) % mod
        for x in (0, 1):
            if singles[x]:
                spot = (x, p)
                fresh[spot] = (fresh.get(spot, 0) + singles[x]) % mod
        for key in fresh:
            pairs[key] = (pairs.get(key, 0) + fresh[key]) % mod
        singles[p] = singles[p] + 1
    return total % mod


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_runs(read_input()))


if __name__ == "__main__":
    main()
