import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return n, k, data[2:2 + n], data[2 + n:2 + 2 * n]

# Clause apply_step [Confidence: 1.00]
def apply_step(goes, sums, lows, step_goes, step_sums, step_lows):
    for i in range(len(goes)):
        j = goes[i]
        sums[i] += step_sums[j]
        if step_lows[j] < lows[i]:
            lows[i] = step_lows[j]
        goes[i] = step_goes[j]

# Clause double_step [Confidence: 1.00]
def double_step(step_goes, step_sums, step_lows):
    n = len(step_goes)
    goes = [0] * n
    sums = [0] * n
    lows = [0] * n
    for i in range(n):
        j = step_goes[i]
        goes[i] = step_goes[j]
        sums[i] = step_sums[i] + step_sums[j]
        lows[i] = step_lows[i] if step_lows[i] < step_lows[j] else step_lows[j]
    return goes, sums, lows

# Clause walk_paths [Confidence: 1.00]
def walk_paths(n, k, f, w):
    goes = list(range(n))
    sums = [0] * n
    lows = [1 << 62] * n
    step_goes = f
    step_sums = w
    step_lows = w
    while k:
        if k & 1:
            apply_step(goes, sums, lows, step_goes, step_sums, step_lows)
        k >>= 1
        if k:
            step_goes, step_sums, step_lows = double_step(step_goes, step_sums, step_lows)
    return sums, lows

# Clause main [Confidence: 1.00]
def main():
    n, k, f, w = read_input()
    sums, lows = walk_paths(n, k, f, w)
    collected = []
    for i in range(n):
        collected.append("%d %d" % (sums[i], lows[i]))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

