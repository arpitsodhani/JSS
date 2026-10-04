import sys

n = sys.stdin.readline().strip()
count = 0

while len(n) > 1:
    n = str(sum(int(c) for c in n))
    count += 1

print(count)
