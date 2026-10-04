from itertools import permutations
import sys

lines = sys.stdin.read().strip().split('\n')
n, k = map(int, lines[0].split())
numbers = [lines[i+1] for i in range(n)]

min_diff = float('inf')

for perm in permutations(range(k)):
    rearranged = [int(''.join(num[perm[i]] for i in range(k))) for num in numbers]
    diff = max(rearranged) - min(rearranged)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
