import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return fields[2:2 + n]


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
    n = len(a)
    total = 0
    from_here = 0
    reach = 0
    counts = {}
    for i in range(n):
        element = a[i]
        counts[element] = counts.get(element, 0) + 1
        if last[element] > reach:
            reach = last[element]
        if i == reach:
            keep = 0
            for other in counts:
                if counts[other] > keep:
                    keep = counts[other]
            total += (i - from_here + 1) - keep
            counts = {}
            from_here = i + 1
    return total


# --- clause: main :: () -> None ---
def main():
    a = read_input()
    first, last = value_spans(a)
    sys.stdout.write("%d\n" % difficulty(a, first, last))


if __name__ == "__main__":
    main()
