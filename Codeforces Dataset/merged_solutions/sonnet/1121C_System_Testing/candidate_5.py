import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    k = raw[1]
    return k, raw[2:2 + n]


# --- clause: schedule :: (k: int, a: list[int]) -> list[tuple[int, int]] ---
def schedule(k, a):
    n = len(a)
    free = [0] * k
    spans = []
    for i in range(n):
        top = 0
        for j in range(1, k):
            if free[j] < free[top]:
                top = j
        head_pos = free[top]
        free[top] = head_pos + a[i]
        spans.append((head_pos, free[top]))
    return spans


# --- clause: count_interesting :: (spans: list[tuple[int, int]]) -> int ---
def count_interesting(spans):
    n = len(spans)
    horizon = max(end for head_pos, end in spans) + 2
    done = [0] * horizon
    for head_pos, end in spans:
        done[end] += 1
    for time in range(1, horizon):
        done[time] += done[time - 1]
    total = 0
    for head_pos, end in spans:
        for time in range(head_pos, end):
            if (200 * done[time] + n) // (2 * n) == time - head_pos + 1:
                total += 1
                break
    return total


# --- clause: main :: () -> None ---
def main():
    k, a = read_input()
    sys.stdout.write("%d\n" % count_interesting(schedule(k, a)))


if __name__ == "__main__":
    main()
