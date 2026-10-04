import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    words = []
    for i in range(t):
        words.append(data[2 * i + 2])
    return words


# --- clause: run_lengths :: (s: bytes) -> list[int] ---
def run_lengths(s):
    n = len(s)
    start = 0
    while start < n and s[start] == s[n - 1]:
        start += 1
    if start == n:
        return [n]
    runs = []
    length = 1
    step = 1
    while step < n:
        i = (start + step) % n
        prev = i - 1 if i else n - 1
        if s[i] != s[prev]:
            runs.append(length)
            length = 0
        length += 1
        step += 1
    runs.append(length)
    return runs


# --- clause: fewest_talks :: (s: bytes) -> int ---
def fewest_talks(s):
    runs = run_lengths(s)
    if len(runs) == 1:
        return (runs[0] + 2) // 3
    total = 0
    for length in runs:
        total += length // 3
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(str(fewest_talks(s)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
