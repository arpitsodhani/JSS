import sys


# --- clause: read_input :: () -> list[list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append([(numbers[cursor + 2 * i], numbers[cursor + 2 * i + 1]) for i in range(n)])
        cursor += 2 * n
    return cases


# --- clause: shortest_bridge :: (segments: list[tuple[int, int]]) -> int ---
def shortest_bridge(segments):
    left = max(a for a, b in segments)
    right = min(b for a, b in segments)
    gap = left - right
    return gap if gap > 0 else 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for segments in read_input():
        out.append(shortest_bridge(segments))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
