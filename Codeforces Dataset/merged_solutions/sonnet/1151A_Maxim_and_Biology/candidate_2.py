import sys


# --- clause: read_input :: () -> tuple[int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), data[1]


# --- clause: letter_cost :: (have: int, want: int) -> int ---
def letter_cost(have, want):
    forward = (have - want) % 26
    backward = (want - have) % 26
    if forward < backward:
        return forward
    return backward


# --- clause: fewest_changes :: (n: int, s: bytes) -> int ---
def fewest_changes(n, s):
    genome = b"ACTG"
    costs = []
    for start in range(n - 3):
        window = 0
        for offset in range(4):
            window += letter_cost(s[start + offset], genome[offset])
        costs.append(window)
    return min(costs)


# --- clause: main :: () -> None ---
def main():
    n, s = read_input()
    sys.stdout.write("%d\n" % fewest_changes(n, s))


if __name__ == "__main__":
    main()
