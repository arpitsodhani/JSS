import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    w = data[1]
    k = data[2]
    return n, w, k, data[3:3 + n], data[3 + n:3 + 2 * n]

# Clause rank_lengths [Confidence: 1.00]
def rank_lengths(t):
    values = sorted(set(t))
    place = {}
    for i in range(len(values)):
        place[values[i]] = i
    ranks = [place[x] for x in t]
    return values, ranks

# Clause top_saving [Confidence: 1.00]
def top_saving(count_tree, half_tree, values, step, window_count, window_halves, w):
    drop = window_count - w
    if drop <= 0:
        return window_halves
    length_of = len(count_tree) - 1
    offset = 0
    rest = drop
    acc = 0
    jump = step
    while jump:
        nxt = offset + jump
        if nxt <= length_of and count_tree[nxt] <= rest:
            rest -= count_tree[nxt]
            acc += half_tree[nxt]
            offset = nxt
        jump >>= 1
    return window_halves - acc - rest * (values[offset] // 2)

# Clause max_pleasure [Confidence: 1.00]
def max_pleasure(n, w, k, a, t, values, ranks):
    length_of = len(values)
    count_tree = [0] * (length_of + 1)
    half_tree = [0] * (length_of + 1)
    step = 1
    while step * 2 <= length_of:
        step *= 2
    left = 0
    window_time = 0
    window_halves = 0
    window_count = 0
    pleasure = 0
    best = 0
    for right in range(n):
        i = ranks[right] + 1
        half = t[right] // 2
        while i <= length_of:
            count_tree[i] += 1
            half_tree[i] += half
            i += i & (-i)
        window_time += t[right]
        window_halves += half
        window_count += 1
        pleasure += a[right]
        while left <= right:
            saving = top_saving(count_tree, half_tree, values, step, window_count, window_halves, w)
            if window_time - saving <= k:
                break
            i = ranks[left] + 1
            gone = t[left] // 2
            while i <= length_of:
                count_tree[i] -= 1
                half_tree[i] -= gone
                i += i & (-i)
            window_time -= t[left]
            window_halves -= gone
            window_count -= 1
            pleasure -= a[left]
            left += 1
        if left <= right and pleasure > best:
            best = pleasure
    return best

# Clause main [Confidence: 1.00]
def main():
    n, w, k, a, t = read_input()
    values, ranks = rank_lengths(t)
    sys.stdout.write("%d\n" % max_pleasure(n, w, k, a, t, values, ranks))


if __name__ == "__main__":
    main()

