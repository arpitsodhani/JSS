import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    length = data[1]
    a = data[2:2 + n]
    k = data[2 + n]
    return n, length, a, k

# Clause best_after_flips [Confidence: 1.00]
def best_after_flips(n, length, a, k):
    negatives = sorted({-v for v in a if v < 0})
    size = len(negatives)
    rank = {}
    for index, value in enumerate(negatives):
        rank[value] = index + 1
    counts = [0] * (size + 1)
    sums = [0] * (size + 1)
    step_start = 1
    while step_start * 2 <= size:
        step_start *= 2
    window = 0
    negative_count = 0
    negative_sum = 0
    best = None
    for i in range(n):
        value = a[i]
        window += value
        if value < 0:
            spot = rank[-value]
            negative_count += 1
            negative_sum -= value
            while spot <= size:
                counts[spot] += 1
                sums[spot] -= value
                spot += spot & -spot
        if i >= length:
            old = a[i - length]
            window -= old
            if old < 0:
                spot = rank[-old]
                negative_count -= 1
                negative_sum += old
                while spot <= size:
                    counts[spot] -= 1
                    sums[spot] += old
                    spot += spot & -spot
        if i >= length - 1:
            keep = negative_count if negative_count < k else k
            drop = negative_count - keep
            small = 0
            need = drop
            spot = 0
            step = step_start
            while step:
                nxt = spot + step
                if nxt <= size and counts[nxt] <= need:
                    need -= counts[nxt]
                    small += sums[nxt]
                    spot = nxt
                step >>= 1
            if need > 0:
                small += need * negatives[spot]
            here = window + 2 * (negative_sum - small)
            if best is None or here > best:
                best = here
    return best

# Clause main [Confidence: 1.00]
def main():
    n, length, a, k = read_input()
    first = best_after_flips(n, length, a, k)
    second = best_after_flips(n, length, [-v for v in a], k)
    sys.stdout.write(str(first if first > second else second) + "\n")


if __name__ == "__main__":
    main()

