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
    while len(periods) < n:
        periods.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    return n, p1, p2, p3, t1, t2, periods


# --- clause: gap_cost :: (gap: int, p1: int, p2: int, p3: int, t1: int, t2: int) -> int ---
def gap_cost(gap, p1, p2, p3, t1, t2):
    first = gap if gap < t1 else t1
    rest = gap - first
    second = rest if rest < t2 else t2
    third = rest - second
    return first * p1 + second * p2 + third * p3


# --- clause: total_power :: (n: int, p1: int, p2: int, p3: int, t1: int, t2: int, periods: list[tuple[int, int]]) -> int ---
def total_power(n, p1, p2, p3, t1, t2, periods):
    total = (periods[0][1] - periods[0][0]) * p1
    index = 1
    while index < n:
        previous = periods[index - 1]
        current = periods[index]
        total += gap_cost(current[0] - previous[1], p1, p2, p3, t1, t2)
        total += (current[1] - current[0]) * p1
        index += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, p1, p2, p3, t1, t2, periods = read_input()
    print(total_power(n, p1, p2, p3, t1, t2, periods))


if __name__ == "__main__":
    main()
