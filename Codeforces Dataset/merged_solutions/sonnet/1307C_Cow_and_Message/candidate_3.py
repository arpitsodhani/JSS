import sys


# --- clause: read_input :: () -> bytes ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0]


# --- clause: best_count :: (s: bytes) -> int ---
def best_count(s):
    n = len(s)
    singles = [0] * 26
    for ch in s:
        singles[ch - 97] += 1
    best = max(singles)
    suffix = [0] * 26
    pairs = [0] * 676
    for i in range(n - 1, -1, -1):
        k = s[i] - 97
        for second in range(26):
            pairs[k * 26 + second] += suffix[second]
        suffix[k] += 1
    for value in pairs:
        if value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    print(best_count(read_input()))


if __name__ == "__main__":
    main()
