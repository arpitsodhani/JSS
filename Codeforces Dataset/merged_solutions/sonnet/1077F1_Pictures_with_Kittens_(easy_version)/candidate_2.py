import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    k = tokens[1]
    x = tokens[2]
    return k, x, tokens[3:3 + n]


# --- clause: best_beauty :: (k: int, x: int, a: list[int]) -> int ---
def best_beauty(k, x, a):
    n = len(a)
    low = -1
    best = [[low] * (n + 1) for _ in range(x + 1)]
    for i in range(1, k + 1):
        if i <= n:
            best[1][i] = a[i - 1]
    for taken in range(2, x + 1):
        for i in range(1, n + 1):
            top = low
            start = i - k if i - k > 0 else 1
            for j in range(start, i):
                if best[taken - 1][j] > top:
                    top = best[taken - 1][j]
            if top > low:
                best[taken][i] = top + a[i - 1]
    result = low
    for i in range(n - k + 1 if n - k + 1 > 1 else 1, n + 1):
        if best[x][i] > result:
            result = best[x][i]
    return result


# --- clause: main :: () -> None ---
def main():
    k, x, a = read_input()
    sys.stdout.write("%d\n" % best_beauty(k, x, a))


if __name__ == "__main__":
    main()
