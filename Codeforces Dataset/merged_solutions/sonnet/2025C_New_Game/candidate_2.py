import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        k = tokens[pos + 1]
        pos += 2
        cases.append((k, tokens[pos:pos + n]))
        pos += n
    return cases


# --- clause: most_cards :: (k: int, a: list[int]) -> int ---
def most_cards(k, a):
    counts = {}
    for item in a:
        counts[item] = counts.get(item, 0) + 1
    values = sorted(counts)
    best = 0
    left = 0
    window = 0
    for right in range(len(values)):
        window += counts[values[right]]
        while values[right] - values[left] > k - 1 or right - left + 1 > k:
            window -= counts[values[left]]
            left += 1
        if window > best:
            best = window
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append(most_cards(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
