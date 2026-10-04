import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: bit_counts :: (x: list[int]) -> list[int] ---
def bit_counts(x):
    counts = [0] * 60
    for value in x:
        while value:
            bottom = value & (-value)
            counts[bottom.bit_length() - 1] += 1
            value -= bottom
    return counts


# --- clause: triple_sum :: (x: list[int], counts: list[int]) -> int ---
def triple_sum(x, counts):
    mod = 1000000007
    n = len(x)
    total = 0
    for value in x:
        left = 0
        right = 0
        for b in range(60):
            if (value >> b) & 1:
                left += (1 << b) * counts[b]
                right += (1 << b) * n
            else:
                right += (1 << b) * counts[b]
        total += (left % mod) * (right % mod)
    return total % mod


# --- clause: main :: () -> None ---
def main():
    out = []
    for x in read_input():
        out.append(triple_sum(x, bit_counts(x)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
