import sys

data = sys.stdin.read().split()
t = int(data[0])

fb = []
for i in range(1, 200):
    if i % 3 == 0:
        fb.append('F')
    if i % 5 == 0:
        fb.append('B')
pattern = ''.join(fb)

ans = []
idx = 1
for _ in range(t):
    n = int(data[idx])
    s = data[idx + 1]
    idx += 2
    ans.append("YES" if s in pattern else "NO")

print('\n'.join(ans))
