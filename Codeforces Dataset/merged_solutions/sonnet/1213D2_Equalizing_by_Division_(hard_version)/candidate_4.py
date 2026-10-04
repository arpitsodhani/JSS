import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return n, k, data[2:2 + n]


# --- clause: fewest_moves :: (n: int, k: int, a: list[int]) -> int ---
def fewest_moves(n, k, a):
    limit = max(a) + 1
    taken = [0] * limit
    price = [0] * limit
    best = 1 << 60
    for value in sorted(a):
        current = value
        steps = 0
        while True:
            if taken[current] < k:
                taken[current] += 1
                price[current] += steps
                if taken[current] == k and price[current] < best:
                    best = price[current]
            if current == 0:
                break
            current = current >> 1
            steps += 1
    return best


# --- clause: main :: () -> None ---
def main():
    n, k, a = read_input()
    sys.stdout.write(str(fewest_moves(n, k, a)) + "\n")


if __name__ == "__main__":
    main()
