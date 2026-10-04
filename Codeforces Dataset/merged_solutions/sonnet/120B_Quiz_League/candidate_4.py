import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    asked = [int(data[i + 2]) for i in range(n)]
    return n, k, asked


# --- clause: find_sector :: (n: int, k: int, asked: list[int]) -> int ---
def find_sector(n, k, asked):
    index = k - 1
    while asked[index] != 1:
        index += 1
        if index == n:
            index = 0
    return index + 1


# --- clause: main :: () -> None ---
def main():
    n, k, asked = read_input()
    sys.stdout.write(str(find_sector(n, k, asked)) + "\n")


if __name__ == "__main__":
    main()
