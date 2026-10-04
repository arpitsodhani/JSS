import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    asked = list(map(int, data[2:n + 2]))
    return n, k, asked


# --- clause: find_sector :: (n: int, k: int, asked: list[int]) -> int ---
def find_sector(n, k, asked):
    index = k - 1
    while not asked[index]:
        index += 1
        if index >= n:
            index = 0
    return index + 1


# --- clause: main :: () -> None ---
def main():
    n, k, asked = read_input()
    sys.stdout.write("%d\n" % find_sector(n, k, asked))


if __name__ == "__main__":
    main()
