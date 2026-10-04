import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    x = numbers[2]
    return k, x, numbers[3:3 + n]


# --- clause: best_beauty :: (k: int, x: int, a: list[int]) -> int ---
def best_beauty(k, x, a):
    n = len(a)
    low = -1
    best = [low] * (n + 1)
    for i in range(1, k + 1):
        if i <= n:
            best[i] = a[i - 1]
    taken = 2
    while taken <= x:
        step = [low] * (n + 1)
        for i in range(1, n + 1):
            top = low
            j = i - 1
            while j >= 1 and j >= i - k:
                if best[j] > top:
                    top = best[j]
                j -= 1
            if top > low:
                step[i] = top + a[i - 1]
        best = step
        taken += 1
    answer = low
    i = n
    while i >= 1 and i > n - k:
        if best[i] > answer:
            answer = best[i]
        i -= 1
    return answer


# --- clause: main :: () -> None ---
def main():
    k, x, a = read_input()
    sys.stdout.write("%d\n" % best_beauty(k, x, a))


if __name__ == "__main__":
    main()
