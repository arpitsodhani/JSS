import sys

t = sys.stdin.readline().strip()
m = len(t)

for n in range(m // 2 + 1, m):
    if t[:n] == t[m - n:]:
        print("YES")
        print(t[:n])
        break
else:
    print("NO")
