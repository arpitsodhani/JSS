import sys

def solve(x0, n):
    r = n % 4
    if x0 % 2 == 0:  # x0 is even
        if r == 0:
            return x0
        elif r == 1:
            return x0 - n
        elif r == 2:
            return x0 + 1
        else:  # r == 3
            return x0 + n + 1
    else:  # x0 is odd
        if r == 0:
            return x0
        elif r == 1:
            return x0 + n
        elif r == 2:
            return x0 - 1
        else:  # r == 3
            return x0 - n - 1

input_data = sys.stdin.read().split()
idx = 0
t = int(input_data[idx])
idx += 1

for _ in range(t):
    x0 = int(input_data[idx])
    n = int(input_data[idx + 1])
    idx += 2
    print(solve(x0, n))
