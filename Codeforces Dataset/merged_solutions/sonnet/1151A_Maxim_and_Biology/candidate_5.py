import sys


# --- clause: read_input :: () -> tuple[int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n, bytes(data[1])


# --- clause: letter_cost :: (have: int, want: int) -> int ---
def letter_cost(have, want):
    gap = have - want
    if gap < 0:
        gap += 26
    return min(gap, 26 - gap)


# --- clause: fewest_changes :: (n: int, s: bytes) -> int ---
def fewest_changes(n, s):
    genome = b"ACTG"
    running = 0
    for offset in range(4):
        running += letter_cost(s[offset], genome[offset])
    best = running
    for start in range(1, n - 3):
        running = 0
        for offset in range(4):
            running += letter_cost(s[start + offset], genome[offset])
        if running < best:
            best = running
    return best


# --- clause: main :: () -> None ---
def main():
    n, s = read_input()
    sys.stdout.write(str(fewest_changes(n, s)) + "\n")


if __name__ == "__main__":
    main()
