import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    numbers = list(map(int, data[2:2 + 2 * n]))
    lows = numbers[0::2]
    highs = numbers[1::2]
    return n, k, lows, highs


# --- clause: lucky_numbers :: () -> list[int] ---
def lucky_numbers():
    found = []
    for width in range(1, 19):
        for mask in range(1 << width):
            value = 0
            for bit in range(width - 1, -1, -1):
                value = value * 10 + (7 if mask >> bit & 1 else 4)
            found.append(value)
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
    span = highs[0] - lows[0]
    for i in range(1, n):
        if highs[i] - lows[i] < span:
            span = highs[i] - lows[i]
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
    sys.stdout.write("%d\n" % best_count(n, k, lows, highs, lucky_numbers()))


if __name__ == "__main__":
    main()
