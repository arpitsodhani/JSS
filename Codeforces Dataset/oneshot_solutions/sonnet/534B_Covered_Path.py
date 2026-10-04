v1, v2 = map(int, input().split())
t, d = map(int, input().split())

# Compute maximum speeds going forward from v1
forward = [0] * t
forward[0] = v1
for i in range(1, t):
    forward[i] = forward[i-1] + d

# Compute maximum speeds going backward from v2
backward = [0] * t
backward[t-1] = v2
for i in range(t-2, -1, -1):
    backward[i] = backward[i+1] + d

# Take minimum at each position and sum
total = 0
for i in range(t):
    total += min(forward[i], backward[i])

print(total)
