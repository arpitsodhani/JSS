import sys

data = sys.stdin.read().split()
idx = 0
t = int(data[idx])
idx += 1

for _ in range(t):
    x1 = int(data[idx])
    x2 = int(data[idx + 1])
    x3 = int(data[idx + 2])
    idx += 3
    
    result = max(x1, x2, x3) - min(x1, x2, x3)
    print(result)
