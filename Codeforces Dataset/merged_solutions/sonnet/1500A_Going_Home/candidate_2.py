import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: find_quadruple :: (n: int, a: list[int]) -> tuple[int, int, int, int] | None ---
def find_quadruple(n, a):
    stored = {}
    for j in range(1, n):
        value = a[j]
        for i in range(j):
            total = value + a[i]
            if total in stored:
                x, y = stored[total]
                if x != i and x != j and y != i and y != j:
                    return x + 1, y + 1, i + 1, j + 1
            else:
                stored[total] = (i, j)
    return None

# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    found = find_quadruple(n, a)
    if found is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%d %d %d %d\n" % found)


if __name__ == "__main__":
    main()
