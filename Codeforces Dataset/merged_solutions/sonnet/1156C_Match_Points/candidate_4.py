import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    z = numbers[1]
    return z, sorted(numbers[2:2 + n])


# --- clause: fits :: (k: int, z: int, spots: list[int]) -> bool ---
def fits(k, z, spots):
    n = len(spots)
    i = 0
    while i < k:
        if spots[n - k + i] - spots[i] < z:
            return False
        i += 1
    return True


# --- clause: most_pairs :: (z: int, spots: list[int]) -> int ---
def most_pairs(z, spots):
    small = 0
    high = len(spots) // 2
    while small < high:
        mid = (small + high + 1) // 2
        if fits(mid, z, spots):
            small = mid
        else:
            high = mid - 1
    return small


# --- clause: main :: () -> None ---
def main():
    z, spots = read_input()
    sys.stdout.write("%d\n" % most_pairs(z, spots))


if __name__ == "__main__":
    main()
