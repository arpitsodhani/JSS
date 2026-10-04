# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = data[p]
    p += 1
    out = []
    for _ in range(t):
        n = data[p]
        k = data[p + 1]
        p += 2
        total = 0
        gains = []
        for i in range(1, n + 1):
            x = data[p]
            p += 1
            total += x
            gains.append(x + i)
        gains.sort(reverse=True)
        ans = total + k * n - k * (k - 1) // 2 - sum(gains[:k])
        out.append(str(ans))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.40]
main()


