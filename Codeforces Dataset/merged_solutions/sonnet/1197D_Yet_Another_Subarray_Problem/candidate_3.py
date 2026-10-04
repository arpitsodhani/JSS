import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    k = fields[2]
    return m, k, fields[3:3 + n]


# --- clause: best_cost :: (m: int, k: int, a: list[int]) -> int ---
def best_cost(m, k, a):
    none = -(1 << 62)
    best = [none] * m
    reply = 0
    for value in a:
        fresh = [none] * m
        start = 1 % m
        fresh[start] = value - k
        for rest in range(m):
            if best[rest] == none:
                continue
            jump = (rest + 1) % m
            here = best[rest] + value
            if jump == start:
                here -= k
            if here > fresh[jump]:
                fresh[jump] = here
        best = fresh
        for rest in range(m):
            if best[rest] > reply:
                reply = best[rest]
    return reply


# --- clause: main :: () -> None ---
def main():
    m, k, a = read_input()
    sys.stdout.write("%d\n" % best_cost(m, k, a))


if __name__ == "__main__":
    main()
