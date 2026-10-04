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
    tally = {}
    for value in a:
        tally[value] = tally.get(value, 0) + 1
    total = 0
    smaller = 0
    for value in sorted(tally):
        c = tally[value]
        total += c * (c - 1) // 2 * smaller
        total += c * (c - 1) * (c - 2) // 6
        smaller += c
    return total

# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(count_triangles(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
