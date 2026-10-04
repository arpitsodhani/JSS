import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])
idx = 2

ip_to_name = {}
for _ in range(n):
    name = data[idx]
    ip = data[idx + 1]
    ip_to_name[ip] = name
    idx += 2

out = []
for _ in range(m):
    command = data[idx]
    ip_semicolon = data[idx + 1]
    ip = ip_semicolon[:-1]
    out.append(f"{command} {ip_semicolon} #{ip_to_name[ip]}")
    idx += 2

sys.stdout.write("\n".join(out))
