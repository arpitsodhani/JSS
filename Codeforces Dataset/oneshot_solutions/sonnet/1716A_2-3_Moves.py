import sys

data = sys.stdin.read().split()
t = int(data[0])
for i in range(1, t + 1):
    n = abs(int(data[i]))
    if n == 0:
        print(0)
    elif n == 1:
        print(2)
    else:
        print((n + 2) // 3)
