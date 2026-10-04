import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    k = data[2]
    segments = []
    pos = 3
    for _ in range(m):
        segments.append((data[pos], data[pos + 1]))
        pos += 2
    return n, m, k, segments


# --- clause: best_total :: (n: int, m: int, k: int, segments: list[tuple[int, int]]) -> int ---
def best_total(n, m, k, segments):
    order = sorted(segments, key=lambda seg: seg[0] + seg[1])
    prefix = [0] * (m + 1)
    suffix = [0] * (m + 1)
    for start in range(1, n - k + 2):
        end = start + k - 1
        running = 0
        for i, (l, r) in enumerate(order):
            lo = l if l > start else start
            hi = r if r < end else end
            if hi >= lo:
                running += hi - lo + 1
            if running > prefix[i + 1]:
                prefix[i + 1] = running
        running = 0
        for i in range(m - 1, -1, -1):
            l, r = order[i]
            lo = l if l > start else start
            hi = r if r < end else end
            if hi >= lo:
                running += hi - lo + 1
            if running > suffix[i]:
                suffix[i] = running
    best = 0
    for i in range(m + 1):
        if prefix[i] + suffix[i] > best:
            best = prefix[i] + suffix[i]
    return best


# --- clause: main :: () -> None ---
def main():
    n, m, k, segments = read_input()
    sys.stdout.write(str(best_total(n, m, k, segments)) + "\n")


if __name__ == "__main__":
    main()
