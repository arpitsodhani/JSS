import sys

n, m = map(int, sys.stdin.read().split())
print(min(n, m, (n + m) // 3))
