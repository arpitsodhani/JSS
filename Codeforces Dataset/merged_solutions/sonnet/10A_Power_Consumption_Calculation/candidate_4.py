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
    for i in range(n):
        left = int(data[6 + 2 * i])
        right = int(data[7 + 2 * i])
        periods.append((left, right))
    return n, p1, p2, p3, t1, t2, periods


# --- clause: gap_cost :: (gap: int, p1: int, p2: int, p3: int, t1: int, t2: int) -> int ---
def gap_cost(gap, p1, p2, p3, t1, t2):
    first = gap if gap < t1 else t1
    rest = gap - first
    second = rest if rest < t2 else t2
    third = rest - second
    return p1 * first + p2 * second + p3 * third


# --- clause: total_power :: (n: int, p1: int, p2: int, p3: int, t1: int, t2: int, periods: list[tuple[int, int]]) -> int ---
def total_power(n, p1, p2, p3, t1, t2, periods):
    total = 0
    for left, right in periods:
        total += (right - left) * p1
    for i in range(1, n):
        idle = periods[i][0] - periods[i - 1][1]
        total += gap_cost(idle, p1, p2, p3, t1, t2)
    return total


# --- clause: main :: () -> None ---
def main():
    n, p1, p2, p3, t1, t2, periods = read_input()
    sys.stdout.write(str(total_power(n, p1, p2, p3, t1, t2, periods)) + "\n")


if __name__ == "__main__":
    main()
