import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1])


# --- clause: color_count :: (n: int, k: int) -> int ---
def color_count(n, k):
    count = 0
    reach = 1
    while n > reach:
        reach *= k
        count += 1
    return count


# --- clause: color_edges :: (n: int, k: int) -> list[int] ---
def color_edges(n, k):
    colors = []
    for a in range(n - 1):
        for b in range(a + 1, n):
            high = a
            low = b
            level = 0
            while high != low:
                high //= k
                low //= k
                level += 1
            colors.append(level)
    return colors


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    count = color_count(n, k)
    colors = color_edges(n, k)
    out = [str(count), " ".join([str(value) for value in colors])]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
