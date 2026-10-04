import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return n, k, data[2:2 + n]


# --- clause: fewest_moves :: (n: int, k: int, a: list[int]) -> int ---
def fewest_moves(n, k, a):
    order = sorted(a)
    limit = order[-1] + 1
    count = [0] * limit
    spent = [0] * limit
    best = -1
    for value in order:
        current = value
        steps = 0
        while current > 0:
            if count[current] < k:
                count[current] += 1
                spent[current] += steps
                if count[current] == k and (best < 0 or spent[current] < best):
                    best = spent[current]
            current //= 2
            steps += 1
        if count[0] < k:
            count[0] += 1
            spent[0] += steps
            if count[0] == k and (best < 0 or spent[0] < best):
                best = spent[0]
    return best


# --- clause: main :: () -> None ---
def main():
    n, k, a = read_input()
    sys.stdout.write(str(fewest_moves(n, k, a)) + "\n")


if __name__ == "__main__":
    main()
