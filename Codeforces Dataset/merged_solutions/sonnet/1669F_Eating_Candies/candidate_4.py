import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        weights = [int(data[pos + i]) for i in range(n)]
        pos += n
        cases.append((n, weights))
    return cases


# --- clause: solve_case :: (n: int, weights: list[int]) -> int ---
def solve_case(n, weights):
    best = 0
    left = 0
    right = n - 1
    left_sum = 0
    right_sum = 0
    while left <= right:
        if left_sum == right_sum:
            eaten = left + (n - 1 - right)
            if eaten > best:
                best = eaten
            left_sum += weights[left]
            left += 1
        elif left_sum < right_sum:
            left_sum += weights[left]
            left += 1
        else:
            right_sum += weights[right]
            right -= 1
    if left_sum == right_sum:
        eaten = left + (n - 1 - right)
        if eaten > best:
            best = eaten
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(solve_case(case[0], case[1])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
