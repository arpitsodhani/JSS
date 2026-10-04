import sys

lines = sys.stdin.read().strip().split('\n')
n = int(lines[0])
patterns = [lines[i+1] for i in range(n)]

length = len(patterns[0])
result = []

for i in range(length):
    chars = set()
    for pattern in patterns:
        if pattern[i] != '?':
            chars.add(pattern[i])
    
    if len(chars) == 0:
        result.append('a')
    elif len(chars) == 1:
        result.append(chars.pop())
    else:
        result.append('?')

print(''.join(result))
