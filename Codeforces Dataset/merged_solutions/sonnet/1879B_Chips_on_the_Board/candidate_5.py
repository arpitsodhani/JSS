import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        a = raw[reader:reader + n]
        reader += n
        b = raw[reader:reader + n]
        reader += n
        cases.append((a, b))
    return cases


# --- clause: cheapest_cover :: (a: list[int], b: list[int]) -> int ---
def cheapest_cover(a, b):
    n = len(a)
    rows = min(a) * n + sum(b)
    columns = min(b) * n + sum(a)
    return rows if rows < columns else columns


# --- clause: main :: () -> None ---
def main():
    lines = []
    for a, b in read_input():
        lines.append(cheapest_cover(a, b))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
