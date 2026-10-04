import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return int(fields[0]), int(fields[1]), int(fields[2]), int(fields[3])


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: candidate_lengths :: (n: int, k: int, a: int, b: int) -> list[int] ---
def candidate_lengths(n, k, a, b):
    bases = set()
    for base in (b - a, b + a, -a - b, a - b):
        bases.add(base % k)
    summed = n * k
    lengths = []
    for base in bases:
        for i in range(n + 1):
            delta = base + i * k
            if 0 < delta <= summed:
                lengths.append(delta)
    return lengths


# --- clause: stop_range :: (n: int, k: int, lengths: list[int]) -> tuple[int, int] ---
def stop_range(n, k, lengths):
    summed = n * k
    low = summed
    high = 1
    for delta in lengths:
        stops = summed // gcd_of(summed, delta)
        if stops < low:
            low = stops
        if stops > high:
            high = stops
    return low, high


# --- clause: main :: () -> None ---
def main():
    n, k, a, b = read_input()
    lengths = candidate_lengths(n, k, a, b)
    low, high = stop_range(n, k, lengths)
    sys.stdout.write("%d %d\n" % (low, high))


if __name__ == "__main__":
    main()
