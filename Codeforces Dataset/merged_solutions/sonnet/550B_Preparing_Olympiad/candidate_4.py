import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    l = int(data[1])
    r = int(data[2])
    x = int(data[3])
    hardness = [int(data[i + 4]) for i in range(n)]
    return n, l, r, x, hardness


# --- clause: count_sets :: (n: int, l: int, r: int, x: int, hardness: list[int]) -> int ---
def count_sets(n, l, r, x, hardness):
    total = 0
    for mask in range(1, 1 << n):
        picked = [hardness[i] for i in range(n) if mask >> i & 1]
        if len(picked) < 2:
            continue
        summed = sum(picked)
        if summed < l or summed > r:
            continue
        if max(picked) - min(picked) >= x:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, l, r, x, hardness = read_input()
    answer = count_sets(n, l, r, x, hardness)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
