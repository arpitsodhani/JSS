import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        k = fields[cursor + 1]
        cursor += 2
        cases.append((k, fields[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: most_cards :: (k: int, a: list[int]) -> int ---
def most_cards(k, a):
    counts = {}
    for element in a:
        counts[element] = counts.get(element, 0) + 1
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
