import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, a, d, m = data[:4]
clients = data[4:4 + m]

i = 1
j = 0
last_open = None
ans = 0

while i <= n or j < m:
    emp_time = i * a if i <= n else 10**30
    client_time = clients[j] if j < m else 10**30

    if emp_time <= client_time:
        t = emp_time
        i += 1
        while j < m and clients[j] == t:
            j += 1
    else:
        t = client_time
        j += 1
        while i <= n and i * a == t:
            i += 1
        while j < m and clients[j] == t:
            j += 1

    if last_open is None or t > last_open + d:
        ans += 1
        last_open = t

print(ans)
