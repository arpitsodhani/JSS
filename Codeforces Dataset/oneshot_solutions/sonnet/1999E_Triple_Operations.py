import sys
input = sys.stdin.readline

def f(n):
    count = 0
    while n > 0:
        n //= 3
        count += 1
    return count

# Precompute f values and prefix sums
MAX_N = 200001
f_values = [f(i) for i in range(MAX_N)]
prefix = [0] * (MAX_N + 1)

for i in range(MAX_N):
    prefix[i+1] = prefix[i] + f_values[i]

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    sum_f = prefix[r+1] - prefix[l]
    ans = f_values[l] + sum_f
    print(ans)
