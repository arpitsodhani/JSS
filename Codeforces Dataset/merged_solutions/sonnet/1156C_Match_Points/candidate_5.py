import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    z = raw[1]
    return z, sorted(raw[2:2 + n])


# --- clause: fits :: (k: int, z: int, spots: list[int]) -> bool ---
def fits(k, z, spots):
    n = len(spots)
    for i in range(k):
        if spots[n - k + i] - spots[i] < z:
            return False
    return True


# --- clause: most_pairs :: (z: int, spots: list[int]) -> int ---
def most_pairs(z, spots):
    floor_value = 0
    top_value = len(spots) // 2
    while floor_value < top_value:
        mid = (floor_value + top_value + 1) // 2
        if fits(mid, z, spots):
            floor_value = mid
        else:
            top_value = mid - 1
    return floor_value


# --- clause: main :: () -> None ---
def main():
    z, spots = read_input()
    sys.stdout.write("%d\n" % most_pairs(z, spots))


if __name__ == "__main__":
    main()
