import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        cases.append(numbers[reader:reader + n])
        reader += n
    return cases


# --- clause: shuffle_shoes :: (sizes: list[int]) -> list[int] | None ---
def shuffle_shoes(sizes):
    n = len(sizes)
    order = list(range(1, n + 1))
    start = 0
    while start < n:
        stop = start
        while stop + 1 < n and sizes[stop + 1] == sizes[start]:
            stop += 1
        if stop == start:
            return None
        for i in range(start, stop + 1):
            order[i] = start + 1 + (i - start + 1) % (stop - start + 1)
        start = stop + 1
    return order


# --- clause: main :: () -> None ---
def main():
    out = []
    for sizes in read_input():
        order = shuffle_shoes(sizes)
        if order is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
