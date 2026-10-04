import sys

data = sys.stdin.read().split()
n = int(data[0])
k = int(data[1])

if k >= n * (n - 1) // 2:
    print("no solution")
else:
    for i in range(n):
        print(0, i)
