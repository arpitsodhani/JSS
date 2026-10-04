import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    return n, m, k


# --- clause: side_pillows :: (beds: int, peak: int) -> int ---
def side_pillows(beds, peak):
    slope = peak - 1
    if slope > beds:
        slope = beds
    if slope < 0:
        slope = 0
    total = slope * peak - slope * (slope + 1) // 2
    return total + (beds - slope)


# --- clause: most_pillows :: (n: int, m: int, k: int) -> int ---
def most_pillows(n, m, k):
    low = 1
    high = m
    while low < high:
        mid = low + (high - low + 1) // 2
        need = mid + side_pillows(k - 1, mid) + side_pillows(n - k, mid)
        if need > m:
            high = mid - 1
        else:
            low = mid
    return low


# --- clause: main :: () -> None ---
def main():
    n, m, k = read_input()
    answer = most_pillows(n, m, k)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
