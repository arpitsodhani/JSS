import sys

data = sys.stdin.read().split()
n = int(data[0])
k = int(data[1])

for i in range(n):
    row = ["0"] * n
    row[i] = str(k)
    print(" ".join(row))
