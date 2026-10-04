import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    a, b = data[idx], data[idx + 1]
    xk, yk = data[idx + 2], data[idx + 3]
    xq, yq = data[idx + 4], data[idx + 5]
    idx += 6

    moves = set()
    for dx in (a, -a):
        for dy in (b, -b):
            moves.add((dx, dy))
            moves.add((dy, dx))

    s1 = {(xk + dx, yk + dy) for dx, dy in moves}
    s2 = {(xq + dx, yq + dy) for dx, dy in moves}

    ans.append(str(len(s1 & s2)))

print("\n".join(ans))
