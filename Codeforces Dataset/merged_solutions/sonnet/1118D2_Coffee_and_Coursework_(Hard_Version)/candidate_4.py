import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    return m, numbers[2:2 + n]


# --- clause: pages_written :: (a: list[int], days: int) -> int ---
def pages_written(a, days):
    summed = 0
    for i in range(len(a)):
        gain = a[i] - i // days
        if gain <= 0:
            break
        summed += gain
    return summed


# --- clause: fewest_days :: (m: int, a: list[int]) -> int ---
def fewest_days(m, a):
    a = sorted(a, reverse=True)
    if sum(a) < m:
        return -1
    low = 1
    high = len(a)
    while low < high:
        mid = (low + high) // 2
        if pages_written(a, mid) >= m:
            high = mid
        else:
            low = mid + 1
    return low


# --- clause: main :: () -> None ---
def main():
    m, a = read_input()
    sys.stdout.write("%d\n" % fewest_days(m, a))


if __name__ == "__main__":
    main()
