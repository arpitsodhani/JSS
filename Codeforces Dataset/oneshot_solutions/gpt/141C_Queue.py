import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

n = int(data[0])
people = []
idx = 1

for _ in range(n):
    name = data[idx]
    a = int(data[idx + 1])
    idx += 2
    people.append((a, name))

people.sort()

queue = []
height = {}

for i, (a, name) in enumerate(people):
    if a > len(queue):
        print(-1)
        sys.exit()
    height[name] = 1000000000 - i
    queue.insert(a, name)

out = []
for name in queue:
    out.append(f"{name} {height[name]}")

print("\n".join(out))
