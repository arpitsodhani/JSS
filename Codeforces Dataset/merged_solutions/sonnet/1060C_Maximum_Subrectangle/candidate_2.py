import sys


# --- clause: read_input :: () -> tuple[list[int], list[int], int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    a = data[2:2 + n]
    b = data[2 + n:2 + n + m]
    x = data[2 + n + m]
    return a, b, x


# --- clause: min_window_sums :: (arr: list[int]) -> list[int] ---
def min_window_sums(arr):
    n = len(arr)
    best = [0] * (n + 1)
    for length in range(1, n + 1):
        window = sum(arr[:length])
        smallest = window
        for i in range(length, n):
            window += arr[i] - arr[i - length]
            if window < smallest:
                smallest = window
        best[length] = smallest
    return best

# --- clause: best_area :: (a: list[int], b: list[int], x: int) -> int ---
def best_area(a, b, x):
    left = min_window_sums(a)
    right = min_window_sums(b)
    answer = 0
    lb = len(right) - 1
    for la in range(1, len(left)):
        if left[la] > x:
            break
        while lb >= 1 and left[la] * right[lb] > x:
            lb -= 1
        if lb < 1:
            break
        area = la * lb
        if area > answer:
            answer = area
    return answer

# --- clause: main :: () -> None ---
def main():
    a, b, x = read_input()
    sys.stdout.write(str(best_area(a, b, x)) + "\n")


if __name__ == "__main__":
    main()
