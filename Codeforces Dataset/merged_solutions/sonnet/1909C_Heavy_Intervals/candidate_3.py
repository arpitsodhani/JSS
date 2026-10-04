import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int], list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        l = fields[cursor:cursor + n]
        cursor += n
        r = fields[cursor:cursor + n]
        cursor += n
        c = fields[cursor:cursor + n]
        cursor += n
        cases.append((l, r, c))
    return cases


# --- clause: match_lengths :: (l: list[int], r: list[int]) -> list[int] ---
def match_lengths(l, r):
    events = []
    for element in l:
        events.append((element, 0))
    for element in r:
        events.append((element, 1))
    events.sort()
    stack = []
    lengths = []
    for element, kind in events:
        if kind == 0:
            stack.append(element)
        else:
            lengths.append(element - stack.pop())
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
