import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    p1 = int(data[1])
    p2 = int(data[2])
    p3 = int(data[3])
    t1 = int(data[4])
    t2 = int(data[5])
    periods = []
    pos = 6
    for _ in range(n):
        left = int(data[pos])
        pos += 1
        right = int(data[pos])
        pos += 1
        periods.append((left, right))
    return n, p1, p2, p3, t1, t2, periods


# --- clause: gap_cost :: (gap: int, p1: int, p2: int, p3: int, t1: int, t2: int) -> int ---
def gap_cost(gap, p1, p2, p3, t1, t2):
    first = t1
    if gap < t1:
        first = gap
    rest = gap - first
    second = t2
    if rest < t2:
        second = rest
    third = rest - second
    return first * p1 + second * p2 + third * p3


# --- clause: total_power :: (n: int, p1: int, p2: int, p3: int, t1: int, t2: int, periods: list[tuple[int, int]]) -> int ---
def total_power(n, p1, p2, p3, t1, t2, periods):
    total = 0
    for left, right in periods:
        total += (right - left) * p1
    for i in range(1, n):
        gap = periods[i][0] - periods[i - 1][1]
        total += gap_cost(gap, p1, p2, p3, t1, t2)
    return total


# --- clause: main :: () -> None ---
def main():
    n, p1, p2, p3, t1, t2, periods = read_input()
    answer = total_power(n, p1, p2, p3, t1, t2, periods)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
