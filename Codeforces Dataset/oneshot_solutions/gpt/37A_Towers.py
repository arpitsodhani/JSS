import sys
from collections import Counter

data = list(map(int, sys.stdin.read().split()))
n = data[0]
bars = data[1:1 + n]

counts = Counter(bars)
print(max(counts.values()), len(counts))
