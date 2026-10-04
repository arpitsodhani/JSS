import sys

lines = sys.stdin.read().strip().split('\n')
n, m = map(int, lines[0].split())
names = [lines[i+1] for i in range(n)]

MOD = 1000000007
result = 1

for k in range(m):
    chars_at_k = set()
    for name in names:
        chars_at_k.add(name[k])
    result = (result * len(chars_at_k)) % MOD

print(result)
