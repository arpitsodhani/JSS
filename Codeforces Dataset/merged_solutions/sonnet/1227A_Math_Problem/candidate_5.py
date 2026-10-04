import sys


# --- clause: read_input :: () -> list[list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append([(raw[reader + 2 * i], raw[reader + 2 * i + 1]) for i in range(n)])
        reader += 2 * n
    return cases


# --- clause: shortest_bridge :: (segments: list[tuple[int, int]]) -> int ---
def shortest_bridge(segments):
    left = segments[0][0]
    high = segments[0][1]
    for a, b in segments:
        if a > left:
            left = a
        if b < high:
            high = b
    if left <= high:
        return 0
    return left - high


# --- clause: main :: () -> None ---
def main():
    out = []
    for segments in read_input():
        out.append(shortest_bridge(segments))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
