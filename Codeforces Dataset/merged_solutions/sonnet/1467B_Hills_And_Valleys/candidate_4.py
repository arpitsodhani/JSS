import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: bumpiness :: (a: list[int], j: int) -> int ---
def bumpiness(a, j):
    if j <= 0 or j >= len(a) - 1:
        return 0
    if a[j] > a[j - 1] and a[j] > a[j + 1]:
        return 1
    if a[j] < a[j - 1] and a[j] < a[j + 1]:
        return 1
    return 0


# --- clause: least_value :: (a: list[int]) -> int ---
def least_value(a):
    n = len(a)
    flags = [0] * n
    for j in range(n):
        flags[j] = bumpiness(a, j)
    total = sum(flags)
    saved = 0
    for i in range(n):
        before = 0
        for j in (i - 1, i, i + 1):
            if 0 <= j < n:
                before += flags[j]
        keep = a[i]
        for source in (i - 1, i + 1):
            if source < 0 or source >= n:
                continue
            a[i] = a[source]
            after = 0
            for j in (i - 1, i, i + 1):
                if 0 <= j < n:
                    after += bumpiness(a, j)
            if before - after > saved:
                saved = before - after
        a[i] = keep
    return total - saved


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(least_value(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
