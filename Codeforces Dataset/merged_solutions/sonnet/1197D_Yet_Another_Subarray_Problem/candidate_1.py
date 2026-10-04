import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    k = data[2]
    return m, k, data[3:3 + n]


# --- clause: best_cost :: (m: int, k: int, a: list[int]) -> int ---
def best_cost(m, k, a):
    none = -(1 << 62)
    best = [none] * m
    answer = 0
    for value in a:
        fresh = [none] * m
        start = 1 % m
        fresh[start] = value - k
        for rest in range(m):
            if best[rest] == none:
                continue
            step = (rest + 1) % m
            here = best[rest] + value
            if step == start:
                here -= k
            if here > fresh[step]:
                fresh[step] = here
        best = fresh
        for rest in range(m):
            if best[rest] > answer:
                answer = best[rest]
    return answer


# --- clause: main :: () -> None ---
def main():
    m, k, a = read_input()
    sys.stdout.write("%d\n" % best_cost(m, k, a))


if __name__ == "__main__":
    main()
