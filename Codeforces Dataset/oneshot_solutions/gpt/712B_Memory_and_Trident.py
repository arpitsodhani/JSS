import sys

s = sys.stdin.readline().strip()

if len(s) % 2:
    print(-1)
else:
    x = s.count('R') - s.count('L')
    y = s.count('U') - s.count('D')
    print((abs(x) + abs(y)) // 2)
