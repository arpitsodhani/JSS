import sys
import math

n, k = map(int, sys.stdin.readline().split())
a, b = map(int, sys.stdin.readline().split())

nk = n * k

# Find possible values of r_s
if a == 0:
    r_s_values = [0]
elif 2 * a == k:
    r_s_values = [a]
else:
    r_s_values = [a, k - a]

# Find possible values of r_{s+l}
if b == 0:
    r_sl_values = [0]
elif 2 * b == k:
    r_sl_values = [b]
else:
    r_sl_values = [b, k - b]

# Find all possible values of l_0
l0_values = set()
for r_s in r_s_values:
    for r_sl in r_sl_values:
        l0 = (r_sl - r_s) % k
        l0_values.add(l0)

# For each l_0, find min and max stops
min_stops = float('inf')
max_stops = 0

for l0 in l0_values:
    if l0 == 0:
        m_range = range(1, n + 1)
    else:
        m_range = range(0, n)
    
    for m in m_range:
        l = l0 + m * k
        g = math.gcd(l, nk)
        stops = nk // g
        min_stops = min(min_stops, stops)
        max_stops = max(max_stops, stops)

print(min_stops, max_stops)
