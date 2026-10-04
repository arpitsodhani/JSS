import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k


# --- clause: color_count :: (n: int, k: int) -> int ---
def color_count(n, k):
    count = 0
    reach = 1
    while reach < n:
        reach *= k
        count += 1
    return count


# --- clause: color_edges :: (n: int, k: int) -> list[int] ---
def color_edges(n, k):
    colors = []
    a = 0
    while a < n:
        for b in range(a + 1, n):
            high = a
            low = b
            level = 0
            while high != low:
                high = high // k
                low = low // k
                level += 1
            colors.append(level)
        a += 1
    return colors


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    count = color_count(n, k)
    colors = color_edges(n, k)
    print(count)
    print(" ".join(map(str, colors)))


if __name__ == "__main__":
    main()
