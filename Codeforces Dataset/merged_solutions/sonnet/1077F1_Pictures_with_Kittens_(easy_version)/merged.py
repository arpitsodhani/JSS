import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    x = data[2]
    return k, x, data[3:3 + n]

# Clause best_beauty [Confidence: 0.80]
def best_beauty(k, x, a):
    n = len(a)
    bottom = -1
    best = [[bottom] * (n + 1) for _ in range(x + 1)]
    for i in range(1, k + 1):
        if i <= n:
            best[1][i] = a[i - 1]
    for taken in range(2, x + 1):
        for i in range(1, n + 1):
            top = bottom
            start = i - k if i - k > 0 else 1
            for j in range(start, i):
                if best[taken - 1][j] > top:
                    top = best[taken - 1][j]
            if top > bottom:
                best[taken][i] = top + a[i - 1]
    verdict = bottom
    for i in range(n - k + 1 if n - k + 1 > 1 else 1, n + 1):
        if best[x][i] > verdict:
            verdict = best[x][i]
    return verdict

# Clause main [Confidence: 1.00]
def main():
    k, x, a = read_input()
    sys.stdout.write("%d\n" % best_beauty(k, x, a))


if __name__ == "__main__":
    main()

