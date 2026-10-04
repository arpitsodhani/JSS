import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    lows = [0] * n
    highs = [0] * n
    pos = 2
    for i in range(n):
        lows[i] = int(data[2 + 2 * i])
        highs[i] = int(data[3 + 2 * i])
    return n, k, lows, highs


# --- clause: lucky_numbers :: () -> list[int] ---
def lucky_numbers():
    found = []
    frontier = [4, 7]
    while frontier:
        nxt = []
        for value in frontier:
            found.append(value)
            if value <= 10 ** 17:
                nxt.append(value * 10 + 4)
                nxt.append(value * 10 + 7)
        frontier = nxt
    found.sort()
    return found


# --- clause: shift_cost :: (low: int, high: int, lows: list[int], low_sum: list[int], highs: list[int], high_sum: list[int]) -> int ---
def shift_cost(low, high, lows, low_sum, highs, high_sum):
    n = len(lows)
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if highs[mid] < high:
            left = mid + 1
        else:
            right = mid
    cost = left * high - high_sum[left]
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if lows[mid] <= low:
            left = mid + 1
        else:
            right = mid
    cost += (low_sum[n] - low_sum[left]) - (n - left) * low
    return cost


# --- clause: best_count :: (n: int, k: int, lows: list[int], highs: list[int], lucky: list[int]) -> int ---
def best_count(n, k, lows, highs, lucky):
    span = min(hi - lo for lo, hi in zip(lows, highs))
    lows = sorted(lows)
    highs = sorted(highs)
    low_sum = [0] * (n + 1)
    high_sum = [0] * (n + 1)
    for i in range(n):
        low_sum[i + 1] = low_sum[i] + lows[i]
        high_sum[i + 1] = high_sum[i] + highs[i]
    total = len(lucky)
    best = 0
    j = 0
    for i in range(total):
        if j < i:
            j = i
        while j < total:
            if lucky[j] - lucky[i] > span:
                break
            if shift_cost(lucky[i], lucky[j], lows, low_sum, highs, high_sum) > k:
                break
            j += 1
        if j - i > best:
            best = j - i
    return best


# --- clause: main :: () -> None ---
def main():
    n, k, lows, highs = read_input()
    lucky = lucky_numbers()
    sys.stdout.write(str(best_count(n, k, lows, highs, lucky)) + "\n")


if __name__ == "__main__":
    main()
