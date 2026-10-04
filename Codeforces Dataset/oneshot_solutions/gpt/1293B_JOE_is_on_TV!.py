import sys

n = int(sys.stdin.readline())
ans = sum(1.0 / i for i in range(1, n + 1))
print(f"{ans:.12f}")
