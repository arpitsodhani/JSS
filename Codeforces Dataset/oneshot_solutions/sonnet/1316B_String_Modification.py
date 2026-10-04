import sys

def transform(s, k):
    s = list(s)
    n = len(s)
    for i in range(n - k + 1):
        s[i:i+k] = s[i:i+k][::-1]
    return ''.join(s)

def solve(s):
    n = len(s)
    results = []
    for k in range(1, n + 1):
        result = transform(s, k)
        results.append((result, k))
    results.sort()
    return results[0]

input_data = sys.stdin.read().split()
ptr = 0
t = int(input_data[ptr])
ptr += 1

for _ in range(t):
    n = int(input_data[ptr])
    ptr += 1
    s = input_data[ptr]
    ptr += 1
    result, k = solve(s)
    print(result)
    print(k)
