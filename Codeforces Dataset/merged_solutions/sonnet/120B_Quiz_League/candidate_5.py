import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    asked = list(map(int, data[2:2 + n]))
    return n, k, asked


# --- clause: find_sector :: (n: int, k: int, asked: list[int]) -> int ---
def find_sector(n, k, asked):
    index = k - 1
    while asked[index] == 0:
        if index + 1 == n:
            index = 0
        else:
            index += 1
    return index + 1


# --- clause: main :: () -> None ---
def main():
    n, k, asked = read_input()
    answer = find_sector(n, k, asked)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
