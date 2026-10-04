import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    k = raw[2]
    return m, k, raw[3:3 + n]


# --- clause: best_cost :: (m: int, k: int, a: list[int]) -> int ---
def best_cost(m, k, a):
    none = -(1 << 62)
    best = [none] * m
    verdict = 0
    for value in a:
        fresh = [none] * m
        start = 1 % m
        fresh[start] = value - k
        for rest in range(m):
            if best[rest] == none:
                continue
            stride = (rest + 1) % m
            here = best[rest] + value
            if stride == start:
                here -= k
            if here > fresh[stride]:
                fresh[stride] = here
        best = fresh
        for rest in range(m):
            if best[rest] > verdict:
                verdict = best[rest]
    return verdict


# --- clause: main :: () -> None ---
def main():
    m, k, a = read_input()
    sys.stdout.write("%d\n" % best_cost(m, k, a))


if __name__ == "__main__":
    main()
