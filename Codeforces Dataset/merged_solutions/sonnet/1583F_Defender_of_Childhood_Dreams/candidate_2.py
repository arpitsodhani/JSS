import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    return n, k


# --- clause: color_count :: (n: int, k: int) -> int ---
def color_count(n, k):
    count = 0
    reach = 1
    while reach < n:
        reach = reach * k
        count = count + 1
    return count


# --- clause: color_edges :: (n: int, k: int) -> list[int] ---
def color_edges(n, k):
    colors = []
    for a in range(n):
        for b in range(a + 1, n):
            first, second = a, b
            level = 0
            while first != second:
                first //= k
                second //= k
                level += 1
            colors.append(level)
    return colors


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    count = color_count(n, k)
    colors = color_edges(n, k)
    sys.stdout.write("%d\n%s\n" % (count, " ".join(map(str, colors))))


if __name__ == "__main__":
    main()
