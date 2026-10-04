import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
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
    out = []
    for a, b in read_input():
        out.append(cheapest_cover(a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
