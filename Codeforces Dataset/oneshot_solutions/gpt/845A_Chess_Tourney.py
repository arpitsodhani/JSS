import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
ratings = sorted(data[1:])

print("YES" if ratings[n] > ratings[n - 1] else "NO")
