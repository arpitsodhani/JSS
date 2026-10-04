import sys

s = ''.join(ch for ch in sys.stdin.read() if ch in '#.')
g = [s[i * 4:(i + 1) * 4] for i in range(4)]

for i in range(3):
    for j in range(3):
        cnt = 0
        for di in range(2):
            for dj in range(2):
                if g[i + di][j + dj] == '#':
                    cnt += 1
        if cnt != 2:
            print("YES")
            sys.exit()

print("NO")
