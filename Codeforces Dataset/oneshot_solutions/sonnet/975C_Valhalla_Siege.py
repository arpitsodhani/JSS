import bisect

n, q = map(int, input().split())
strengths = list(map(int, input().split()))
arrows = list(map(int, input().split()))

# Prefix sums: prefix[i] = sum of strengths[0..i-1]
prefix = [0]
for s in strengths:
    prefix.append(prefix[-1] + s)

total_strength = prefix[n]
cumulative_arrows = 0

for k in arrows:
    cumulative_arrows += k
    
    if cumulative_arrows >= total_strength:
        # All warriors fell and were resurrected
        cumulative_arrows = 0
        print(n)
    else:
        # Find how many warriors have completely fallen
        # using binary search on prefix sums
        fallen = bisect.bisect_right(prefix, cumulative_arrows) - 1
        print(n - fallen)
