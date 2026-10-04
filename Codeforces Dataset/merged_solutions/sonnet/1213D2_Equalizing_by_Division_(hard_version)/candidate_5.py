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
    limit = max(a) + 1
    filled = [0] * limit
    weight = [0] * limit
    answer = -1
    for value in order:
        current = value
        steps = 0
        while True:
            if filled[current] < k:
                filled[current] += 1
                weight[current] += steps
                if filled[current] == k:
                    if answer < 0 or weight[current] < answer:
                        answer = weight[current]
            if current == 0:
                break
            current //= 2
            steps += 1
    return answer


# --- clause: main :: () -> None ---
def main():
    n, k, a = read_input()
    sys.stdout.write(str(fewest_moves(n, k, a)) + "\n")


if __name__ == "__main__":
    main()
