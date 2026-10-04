import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    l = int(data[1])
    r = int(data[2])
    x = int(data[3])
    hardness = list(map(int, data[4:4 + n]))
    return n, l, r, x, hardness


# --- clause: count_sets :: (n: int, l: int, r: int, x: int, hardness: list[int]) -> int ---
def count_sets(n, l, r, x, hardness):
    order = sorted(range(n), key=lambda i: hardness[i])
    values = [hardness[i] for i in order]
    total = 0
    for mask in range(1, 1 << n):
        summed = 0
        first = -1
        last = -1
        chosen = 0
        for i in range(n):
            if mask >> i & 1:
                summed += values[i]
                if first < 0:
                    first = i
                last = i
                chosen += 1
        if chosen < 2:
            continue
        if l <= summed <= r and values[last] - values[first] >= x:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, l, r, x, hardness = read_input()
    sys.stdout.write(str(count_sets(n, l, r, x, hardness)) + "\n")


if __name__ == "__main__":
    main()
