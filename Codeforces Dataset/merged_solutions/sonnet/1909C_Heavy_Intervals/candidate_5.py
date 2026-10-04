import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int], list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        l = raw[offset:offset + n]
        offset += n
        r = raw[offset:offset + n]
        offset += n
        c = raw[offset:offset + n]
        offset += n
        cases.append((l, r, c))
    return cases


# --- clause: match_lengths :: (l: list[int], r: list[int]) -> list[int] ---
def match_lengths(l, r):
    events = []
    for number in l:
        events.append((number, 0))
    for number in r:
        events.append((number, 1))
    events.sort()
    stack = []
    lengths = []
    for number, kind in events:
        if kind == 0:
            stack.append(number)
        else:
            lengths.append(number - stack.pop())
    return lengths


# --- clause: least_weight :: (lengths: list[int], c: list[int]) -> int ---
def least_weight(lengths, c):
    lengths.sort()
    costs = sorted(c, reverse=True)
    total = 0
    for i in range(0, len(lengths)):
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
