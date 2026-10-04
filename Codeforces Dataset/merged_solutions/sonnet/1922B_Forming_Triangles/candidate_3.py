import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# --- clause: count_triangles :: (a: list[int]) -> int ---
def count_triangles(a):
    n = len(a)
    counts = [0] * (n + 1)
    for value in a:
        counts[value] += 1
    total = 0
    seen = 0
    for value in range(n + 1):
        c = counts[value]
        if c > 1:
            pairs = c * (c - 1) // 2
            total += pairs * seen
            if c > 2:
                total += pairs * (c - 2) // 3
        seen += c
    return total

# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(count_triangles(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
