import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        m = numbers[reader + 1]
        d = numbers[reader + 2]
        reader += 3
        p = numbers[reader:reader + n]
        reader += n
        a = numbers[reader:reader + m]
        reader += m
        cases.append((d, p, a))
    return cases


# --- clause: least_moves :: (d: int, p: list[int], a: list[int]) -> int ---
def least_moves(d, p, a):
    n = len(p)
    where = {}
    for i in range(n):
        where[p[i]] = i + 1
    answers = []
    i = 0
    while i + 1 < len(a):
        x = where[a[i]]
        y = where[a[i + 1]]
        if x >= y or y > x + d:
            return 0
        options = [y - x]
        if d + 1 - (y - x) <= (x - 1) + (n - y):
            options.append(d + 1 - (y - x))
        answers.append(min(options))
        i += 1
    if not answers:
        return 0
    return min(answers)


# --- clause: main :: () -> None ---
def main():
    out = []
    for d, p, a in read_input():
        out.append(least_moves(d, p, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
