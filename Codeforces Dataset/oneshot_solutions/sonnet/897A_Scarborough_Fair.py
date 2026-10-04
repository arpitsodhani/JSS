import sys

input_data = sys.stdin.read().split()
idx = 0

n = int(input_data[idx])
idx += 1
m = int(input_data[idx])
idx += 1

s = list(input_data[idx])
idx += 1

for _ in range(m):
    l = int(input_data[idx])
    idx += 1
    r = int(input_data[idx])
    idx += 1
    c1 = input_data[idx]
    idx += 1
    c2 = input_data[idx]
    idx += 1
    
    for i in range(l - 1, r):
        if s[i] == c1:
            s[i] = c2

print(''.join(s))
