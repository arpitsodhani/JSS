import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    l = int(data[1])
    r = int(data[2])
    x = int(data[3])
    hardness = []
    for token in data[4:n + 4]:
        hardness.append(int(token))
    return n, l, r, x, hardness


# --- clause: count_sets :: (n: int, l: int, r: int, x: int, hardness: list[int]) -> int ---
def count_sets(n, l, r, x, hardness):
    total = 0
    stack = [(0, 0, 0, 1 << 30, -1)]
    while stack:
        i, taken, summed, low, high = stack.pop()
        if i == n:
            if taken >= 2 and l <= summed <= r and high - low >= x:
                total += 1
            continue
        stack.append((i + 1, taken, summed, low, high))
        value = hardness[i]
        new_low = low if low < value else value
        new_high = high if high > value else value
        if summed + value <= r:
            stack.append((i + 1, taken + 1, summed + value, new_low, new_high))
    return total


# --- clause: main :: () -> None ---
def main():
    n, l, r, x, hardness = read_input()
    print(count_sets(n, l, r, x, hardness))


if __name__ == "__main__":
    main()
