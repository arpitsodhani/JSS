import sys


# --- clause: read_input :: () -> list[list[tuple[int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append([(fields[offset + 2 * i], fields[offset + 2 * i + 1]) for i in range(n)])
        offset += 2 * n
    return cases


# --- clause: shortest_bridge :: (segments: list[tuple[int, int]]) -> int ---
def shortest_bridge(segments):
    left = segments[0][0]
    stop = segments[0][1]
    for a, b in segments:
        if a > left:
            left = a
        if b < stop:
            stop = b
    if left <= stop:
        return 0
    return left - stop


# --- clause: main :: () -> None ---
def main():
    out = []
    for segments in read_input():
        out.append(shortest_bridge(segments))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
