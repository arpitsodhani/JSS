import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return numbers[2:2 + n]


# --- clause: value_spans :: (a: list[int]) -> tuple[dict[int, int], dict[int, int]] ---
def value_spans(a):
    first = {}
    last = {}
    for i in range(len(a)):
        if a[i] not in first:
            first[a[i]] = i
        last[a[i]] = i
    return first, last


# --- clause: difficulty :: (a: list[int], first: dict[int, int], last: dict[int, int]) -> int ---
def difficulty(a, first, last):
    spans = sorted((first[value], last[value]) for value in first)
    blocks = []
    for low, high in spans:
        if blocks and low <= blocks[-1][1]:
            if high > blocks[-1][1]:
                blocks[-1][1] = high
        else:
            blocks.append([low, high])
    total = 0
    for low, high in blocks:
        counts = {}
        for i in range(low, high + 1):
            counts[a[i]] = counts.get(a[i], 0) + 1
        keep = 0
        for value in counts:
            if counts[value] > keep:
                keep = counts[value]
        total += high - low + 1 - keep
    return total


# --- clause: main :: () -> None ---
def main():
    a = read_input()
    first, last = value_spans(a)
    sys.stdout.write("%d\n" % difficulty(a, first, last))


if __name__ == "__main__":
    main()
