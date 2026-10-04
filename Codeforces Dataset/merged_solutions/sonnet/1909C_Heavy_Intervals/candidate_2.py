import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int], list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        l = tokens[pos:pos + n]
        pos += n
        r = tokens[pos:pos + n]
        pos += n
        c = tokens[pos:pos + n]
        pos += n
        cases.append((l, r, c))
    return cases


# --- clause: match_lengths :: (l: list[int], r: list[int]) -> list[int] ---
def match_lengths(l, r):
    events = []
    for item in l:
        events.append((item, 0))
    for item in r:
        events.append((item, 1))
    events.sort()
    stack = []
    lengths = []
    for item, kind in events:
        if kind == 0:
            stack.append(item)
        else:
            lengths.append(item - stack.pop())
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
