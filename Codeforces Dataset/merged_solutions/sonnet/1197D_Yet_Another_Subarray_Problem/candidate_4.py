import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    k = numbers[2]
    return m, k, numbers[3:3 + n]


# --- clause: best_cost :: (m: int, k: int, a: list[int]) -> int ---
def best_cost(m, k, a):
    n = len(a)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    none = 1 << 62
    lowest = [none] * m
    answer = 0
    for r in range(n):
        left = r
        value = m * prefix[left] - k * left
        if value < lowest[left % m]:
            lowest[left % m] = value
        head = m * prefix[r + 1] - k * r
        for c in range(m):
            if lowest[c] == none:
                continue
            gap = (r - c) % m
            here = head - lowest[c] - k * (m - gap)
            if here > answer * m:
                answer = here // m
    return answer


# --- clause: main :: () -> None ---
def main():
    m, k, a = read_input()
    sys.stdout.write("%d\n" % best_cost(m, k, a))


if __name__ == "__main__":
    main()
