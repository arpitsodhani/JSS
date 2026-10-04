import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(data[i + 1]) for i in range(n)]
    return n, values


# --- clause: best_power :: (n: int, values: list[int]) -> tuple[int, int] ---
def best_power(n, values):
    best = 1
    for value in values:
        power = value & -value
        if power > best:
            best = power
    count = 0
    for value in values:
        if value & (best - 1):
            continue
        count += 1
    return best, count


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    answer = best_power(n, values)
    power, count = answer[0], answer[1]
    sys.stdout.write("%d %d\n" % (power, count))


if __name__ == "__main__":
    main()
