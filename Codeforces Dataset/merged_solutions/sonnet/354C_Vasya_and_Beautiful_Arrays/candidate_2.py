# CLAUSE: setup_environment
import sys

def read_values():
    return list(map(int, sys.stdin.buffer.read().split()))

# CLAUSE: solve_logic
def possible(divisor, upper, total, prefix, limit):
    count = 0
    left = divisor
    while left <= upper:
        right = left + limit
        block_end = left + divisor - 1
        if right > block_end:
            right = block_end
        if right > upper:
            right = upper
        count += prefix[right] - prefix[left - 1]
        if count == total:
            return True
        left += divisor
    return False

def main():
    data = read_values()
    n = data[0]
    k = data[1]
    arr = data[2:]
    high = max(arr)
    low = min(arr)
    freq = [0] * (high + 1)
    for value in arr:
        freq[value] += 1
    prefix = [0] * (high + 1)
    running = 0
    for value in range(high + 1):
        running += freq[value]
        prefix[value] = running
    for divisor in range(low, 0, -1):
        if possible(divisor, high, n, prefix, k):
            sys.stdout.write(str(divisor))
            return

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
