import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        l = numbers[reader:reader + n]
        reader += n
        r = numbers[reader:reader + n]
        reader += n
        c = numbers[reader:reader + n]
        reader += n
        cases.append((l, r, c))
    return cases


# --- clause: match_lengths :: (l: list[int], r: list[int]) -> list[int] ---
def match_lengths(l, r):
    opens = sorted(l)
    closes = sorted(r)
    stack = []
    lengths = []
    i = 0
    j = 0
    while j < len(closes):
        while i < len(opens) and opens[i] < closes[j]:
            stack.append(opens[i])
            i += 1
        lengths.append(closes[j] - stack.pop())
        j += 1
    return lengths


# --- clause: least_weight :: (lengths: list[int], c: list[int]) -> int ---
def least_weight(lengths, c):
    lengths.sort()
    costs = sorted(c, reverse=True)
    total = 0
    for i in range(len(lengths)):
        total += lengths[i] * costs[i]
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for l, r, c in read_input():
        out.append(least_weight(match_lengths(l, r), c))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
