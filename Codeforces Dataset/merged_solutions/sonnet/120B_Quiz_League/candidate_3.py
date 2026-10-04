import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    asked = []
    for token in data[2:n + 2]:
        asked.append(int(token))
    return n, k, asked


# --- clause: find_sector :: (n: int, k: int, asked: list[int]) -> int ---
def find_sector(n, k, asked):
    index = k - 1
    while asked[index] == 0:
        index = (index + 1) % n
    return index + 1


# --- clause: main :: () -> None ---
def main():
    n, k, asked = read_input()
    print(find_sector(n, k, asked))


if __name__ == "__main__":
    main()
