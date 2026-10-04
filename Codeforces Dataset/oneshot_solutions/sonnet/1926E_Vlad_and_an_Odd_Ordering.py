import sys

def solve(n, k):
    result = 1
    while k > (n + 1) // 2:
        k -= (n + 1) // 2
        n //= 2
        result *= 2
    return result * (2 * k - 1)

input_data = sys.stdin.read().split()
idx = 0
t = int(input_data[idx])
idx += 1
for _ in range(t):
    n = int(input_data[idx])
    k = int(input_data[idx + 1])
    idx += 2
    print(solve(n, k))
