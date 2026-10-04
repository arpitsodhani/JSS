import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append(tokens[at:at + n])
        at += n
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
    total = 0
    for j in range(n):
        total += bumpiness(a, j)
    saved = 0
    for i in range(n):
        before = bumpiness(a, i - 1) + bumpiness(a, i) + bumpiness(a, i + 1)
        keep = a[i]
        for j in (i - 1, i + 1):
            if j < 0 or j >= n:
                continue
            a[i] = a[j]
            after = bumpiness(a, i - 1) + bumpiness(a, i) + bumpiness(a, i + 1)
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
