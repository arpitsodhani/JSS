import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: count_inversions :: (a: list[int]) -> int ---
def count_inversions(a):
    ones = 0
    total = 0
    for entry in a:
        if entry:
            ones += 1
        else:
            total += ones
    return total


# --- clause: best_after_flip :: (a: list[int]) -> int ---
def best_after_flip(a):
    best = count_inversions(a)
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1
            here = count_inversions(a)
            a[i] = 0
            if here > best:
                best = here
            break
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 1:
            a[i] = 0
            here = count_inversions(a)
            a[i] = 1
            if here > best:
                best = here
            break
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(best_after_flip(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
