import sys


# --- clause: read_input :: () -> bytes ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0]


# --- clause: best_count :: (s: bytes) -> int ---
def best_count(s):
    singles = [0] * 26
    pairs = [0] * 676
    best = 0
    for ch in s:
        k = ch - 97
        for first in range(26):
            pairs[first * 26 + k] += singles[first]
        singles[k] += 1
        if singles[k] > best:
            best = singles[k]
    for value in pairs:
        if value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(best_count(read_input())) + "\n")


if __name__ == "__main__":
    main()
