import sys


# --- clause: read_input :: () -> bytes ---
def read_input():
    data = sys.stdin.buffer.read().split()
    word = data[0]
    return word


# --- clause: best_count :: (s: bytes) -> int ---
def best_count(s):
    singles = [0] * 26
    pairs = [0] * 676
    best = 0
    for ch in s:
        k = ch - 97
        base = k
        for first in range(26):
            if singles[first]:
                pairs[first * 26 + base] += singles[first]
        singles[k] += 1
        if singles[k] > best:
            best = singles[k]
    for value in pairs:
        if value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % best_count(read_input()))


if __name__ == "__main__":
    main()
