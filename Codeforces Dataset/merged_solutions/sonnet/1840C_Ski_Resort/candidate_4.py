import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        k = numbers[reader + 1]
        q = numbers[reader + 2]
        reader += 3
        cases.append((k, q, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: count_vacations :: (k: int, q: int, a: list[int]) -> int ---
def count_vacations(k, q, a):
    total = 0
    start = 0
    n = len(a)
    while start < n:
        if a[start] > q:
            start += 1
            continue
        stop = start
        while stop < n and a[stop] <= q:
            stop += 1
        run = stop - start
        if run >= k:
            spare = run - k + 1
            total += spare * (spare + 1) // 2
        start = stop
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, q, a in read_input():
        out.append(count_vacations(k, q, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
