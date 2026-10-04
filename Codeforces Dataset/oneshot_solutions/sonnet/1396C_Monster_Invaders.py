import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, r1, r2, r3, d = data[:5]
    a = data[5:]
    
    full = [0] * n
    partial = [0] * n
    
    for i in range(n):
        full[i] = min(a[i] * r1 + r3, (a[i] + 2) * r1)
        partial[i] = min((a[i] + 1) * r1, r2)
    
    inf = 10 ** 30
    dp0 = 0
    dp1 = inf
    
    for i in range(n - 1):
        new0 = min(dp0 + full[i] + d, dp1 + full[i] + 2 * d)
        new1 = min(dp0 + partial[i] + 2 * d, dp1 + partial[i] + 2 * d)
        dp0, dp1 = new0, new1
    
    last = n - 1
    answer = min(
        dp0 + full[last],
        dp1 + full[last] + d,
        dp0 + partial[last] + r1,
        dp1 + partial[last] + r1 + d
    )
    
    print(answer)

if __name__ == "__main__":
    main()
