import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    k = tokens[1]
    return k, tokens[2:2 + n]


# --- clause: best_average :: (k: int, a: list[int]) -> float ---
def best_average(k, a):
    n = len(a)
    running_sum = [0] * (n + 1)
    for i in range(n):
        running_sum[i + 1] = running_sum[i] + a[i]
    best = 0.0
    for length in range(k, n + 1):
        for start in range(n - length + 1):
            value = (running_sum[start + length] - running_sum[start]) / float(length)
            if value > best:
                best = value
    return best


# --- clause: main :: () -> None ---
def main():
    k, a = read_input()
    sys.stdout.write("%.15f\n" % best_average(k, a))


if __name__ == "__main__":
    main()
