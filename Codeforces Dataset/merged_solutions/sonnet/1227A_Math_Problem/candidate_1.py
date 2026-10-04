import sys


# --- clause: read_input :: () -> list[list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append([(data[pos + 2 * i], data[pos + 2 * i + 1]) for i in range(n)])
        pos += 2 * n
    return cases


# --- clause: shortest_bridge :: (segments: list[tuple[int, int]]) -> int ---
def shortest_bridge(segments):
    left = segments[0][0]
    right = segments[0][1]
    for a, b in segments:
        if a > left:
            left = a
        if b < right:
            right = b
    if left <= right:
        return 0
    return left - right


# --- clause: main :: () -> None ---
def main():
    out = []
    for segments in read_input():
        out.append(shortest_bridge(segments))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
