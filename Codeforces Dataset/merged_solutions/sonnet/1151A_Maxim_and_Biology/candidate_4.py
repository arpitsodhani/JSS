import sys


# --- clause: read_input :: () -> tuple[int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    return n, s


# --- clause: letter_cost :: (have: int, want: int) -> int ---
def letter_cost(have, want):
    table = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
             12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    return table[(have - want) % 26]


# --- clause: fewest_changes :: (n: int, s: bytes) -> int ---
def fewest_changes(n, s):
    genome = b"ACTG"
    best = -1
    for start in range(n - 4, -1, -1):
        total = 0
        for offset in range(4):
            total += letter_cost(s[start + offset], genome[offset])
        if best < 0 or total < best:
            best = total
    return best


# --- clause: main :: () -> None ---
def main():
    n, s = read_input()
    answer = fewest_changes(n, s)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
