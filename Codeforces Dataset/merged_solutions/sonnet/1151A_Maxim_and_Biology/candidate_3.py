import sys


# --- clause: read_input :: () -> tuple[int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1][:n]
    return n, s


# --- clause: letter_cost :: (have: int, want: int) -> int ---
def letter_cost(have, want):
    steps = 0
    walk = have
    while walk != want:
        walk += 1
        if walk > 90:
            walk = 65
        steps += 1
    if steps > 26 - steps:
        return 26 - steps
    return steps


# --- clause: fewest_changes :: (n: int, s: bytes) -> int ---
def fewest_changes(n, s):
    genome = b"ACTG"
    best = -1
    for start in range(n - 3):
        total = 0
        for offset in range(4):
            total += letter_cost(s[start + offset], genome[offset])
        if best < 0 or total < best:
            best = total
    return best


# --- clause: main :: () -> None ---
def main():
    n, s = read_input()
    print(fewest_changes(n, s))


if __name__ == "__main__":
    main()
