import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    k = raw[1]
    return k, raw[2:2 + n]


# --- clause: best_average :: (k: int, a: list[int]) -> float ---
def best_average(k, a):
    n = len(a)
    totals = [0] * (n + 1)
    for i in range(n):
        totals[i + 1] = totals[i] + a[i]
    best = 0.0
    for length in range(k, n + 1):
        for start in range(n - length + 1):
            item = (totals[start + length] - totals[start]) / float(length)
            if item > best:
                best = item
    return best


# --- clause: main :: () -> None ---
def main():
    k, a = read_input()
    sys.stdout.write("%.15f\n" % best_average(k, a))


if __name__ == "__main__":
    main()
