import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    k = fields[1]
    return k, fields[2:2 + n]


# --- clause: schedule :: (k: int, a: list[int]) -> list[tuple[int, int]] ---
def schedule(k, a):
    n = len(a)
    free = [0] * k
    spans = []
    for i in range(n):
        finest = 0
        for j in range(1, k):
            if free[j] < free[finest]:
                finest = j
        opening = free[finest]
        free[finest] = opening + a[i]
        spans.append((opening, free[finest]))
    return spans


# --- clause: count_interesting :: (spans: list[tuple[int, int]]) -> int ---
def count_interesting(spans):
    n = len(spans)
    horizon = max(end for opening, end in spans) + 2
    done = [0] * horizon
    for opening, end in spans:
        done[end] += 1
    for time in range(1, horizon):
        done[time] += done[time - 1]
    total = 0
    for opening, end in spans:
        for time in range(opening, end):
            if (200 * done[time] + n) // (2 * n) == time - opening + 1:
                total += 1
                break
    return total


# --- clause: main :: () -> None ---
def main():
    k, a = read_input()
    sys.stdout.write("%d\n" % count_interesting(schedule(k, a)))


if __name__ == "__main__":
    main()
