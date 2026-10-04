import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    k = fields[1]
    return k, fields[2:2 + n]


# --- clause: best_average :: (k: int, a: list[int]) -> float ---
def best_average(k, a):
    n = len(a)
    cumulative = [0] * (n + 1)
    for i in range(n):
        cumulative[i + 1] = cumulative[i] + a[i]
    best = 0.0
    for length in range(k, n + 1):
        for start in range(n - length + 1):
            entry = (cumulative[start + length] - cumulative[start]) / float(length)
            if entry > best:
                best = entry
    return best


# --- clause: main :: () -> None ---
def main():
    k, a = read_input()
    sys.stdout.write("%.15f\n" % best_average(k, a))


if __name__ == "__main__":
    main()
