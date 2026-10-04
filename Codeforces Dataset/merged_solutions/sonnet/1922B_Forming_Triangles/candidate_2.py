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
    order = sorted(a)
    n = len(order)
    total = 0
    i = 0
    while i < n:
        j = i
        while j < n and order[j] == order[i]:
            j += 1
        same = j - i
        if same >= 2:
            total += same * (same - 1) // 2 * i
        if same >= 3:
            total += same * (same - 1) * (same - 2) // 6
        i = j
    return total

# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(count_triangles(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
