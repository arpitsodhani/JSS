import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    z = data[1]
    return z, sorted(data[2:2 + n])


# --- clause: fits :: (k: int, z: int, spots: list[int]) -> bool ---
def fits(k, z, spots):
    n = len(spots)
    for i in range(k):
        if spots[n - k + i] - spots[i] < z:
            return False
    return True


# --- clause: most_pairs :: (z: int, spots: list[int]) -> int ---
def most_pairs(z, spots):
    low = 0
    high = len(spots) // 2
    while low < high:
        mid = (low + high + 1) // 2
        if fits(mid, z, spots):
            low = mid
        else:
            high = mid - 1
    return low


# --- clause: main :: () -> None ---
def main():
    z, spots = read_input()
    sys.stdout.write("%d\n" % most_pairs(z, spots))


if __name__ == "__main__":
    main()
