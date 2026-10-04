import sys

data = sys.stdin.read().strip().split()

if not data:
    sys.exit()

if len(data) >= 2:
    s = data[1].strip()
else:
    token = data[0].strip()
    i = 0
    while i < len(token) and token[i].isdigit():
        i += 1
    s = token[i:]

x = y = 0
ans = 0
last_side = 0

for ch in s:
    if ch == 'U':
        y += 1
    else:
        x += 1

    side = 1 if y > x else -1 if x > y else 0

    if side == 0:
        continue

    if last_side != 0 and side != last_side:
        ans += 1

    last_side = side

print(ans)
