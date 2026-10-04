import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    return k, numbers[2:2 + n]


# --- clause: best_average :: (k: int, a: list[int]) -> float ---
def best_average(k, a):
    n = len(a)
    best = 0.0
    for start in range(n):
        total = 0
        for end in range(start, n):
            total += a[end]
            width = end - start + 1
            if width < k:
                continue
            value = total / float(width)
            if value > best:
                best = value
    return best


# --- clause: main :: () -> None ---
def main():
    k, a = read_input()
    sys.stdout.write("%.15f\n" % best_average(k, a))


if __name__ == "__main__":
    main()
