import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    return k, numbers[2:2 + n]


# --- clause: schedule :: (k: int, a: list[int]) -> list[tuple[int, int]] ---
def schedule(k, a):
    n = len(a)
    free = [0] * k
    spans = []
    for i in range(n):
        best = 0
        for j in range(1, k):
            if free[j] < free[best]:
                best = j
        from_here = free[best]
        free[best] = from_here + a[i]
        spans.append((from_here, free[best]))
    return spans


# --- clause: count_interesting :: (spans: list[tuple[int, int]]) -> int ---
def count_interesting(spans):
    import bisect

    n = len(spans)
    finish = sorted(end for start, end in spans)
    total = 0
    for start, end in spans:
        time = start
        while time < end:
            ready = bisect.bisect_right(finish, time)
            if (200 * ready + n) // (2 * n) == time - start + 1:
                total += 1
                break
            time += 1
    return total


# --- clause: main :: () -> None ---
def main():
    k, a = read_input()
    sys.stdout.write("%d\n" % count_interesting(schedule(k, a)))


if __name__ == "__main__":
    main()
