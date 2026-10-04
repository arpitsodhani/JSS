import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    w = data[1]
    k = data[2]
    return n, w, k, data[3:3 + n], data[3 + n:3 + 2 * n]


# --- clause: rank_lengths :: (t: list[int]) -> tuple[list[int], list[int]] ---
def rank_lengths(t):
    values = sorted(set(t))
    place = {}
    for i in range(len(values)):
        place[values[i]] = i
    ranks = [place[x] for x in t]
    return values, ranks


# --- clause: top_saving :: (count_tree: list[int], half_tree: list[int], values: list[int], step: int, window_count: int, window_halves: int, w: int) -> int ---
def top_saving(count_tree, half_tree, values, step, window_count, window_halves, w):
    drop = window_count - w
    if drop <= 0:
        return window_halves
    size = len(count_tree) - 1
    pos = 0
    rest = drop
    acc = 0
    jump = step
    while jump:
        nxt = pos + jump
        if nxt <= size and count_tree[nxt] <= rest:
            rest -= count_tree[nxt]
            acc += half_tree[nxt]
            pos = nxt
        jump >>= 1
    return window_halves - acc - rest * (values[pos] // 2)


# --- clause: max_pleasure :: (n: int, w: int, k: int, a: list[int], t: list[int], values: list[int], ranks: list[int]) -> int ---
def max_pleasure(n, w, k, a, t, values, ranks):
    size = len(values)
    count_tree = [0] * (size + 1)
    half_tree = [0] * (size + 1)
    step = 1
    while step * 2 <= size:
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
        while i <= size:
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
            while i <= size:
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


# --- clause: main :: () -> None ---
def main():
    n, w, k, a, t = read_input()
    values, ranks = rank_lengths(t)
    sys.stdout.write("%d\n" % max_pleasure(n, w, k, a, t, values, ranks))


if __name__ == "__main__":
    main()
