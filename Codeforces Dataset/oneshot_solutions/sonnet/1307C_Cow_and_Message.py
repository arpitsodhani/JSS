s = input().strip()
n = len(s)

from collections import defaultdict

max_count = 0

# Count single characters
char_count = defaultdict(int)
for c in s:
    char_count[c] += 1
    max_count = max(max_count, char_count[c])

# Count two-character pairs
pair_count = defaultdict(int)
prefix_count = defaultdict(int)
for i in range(n):
    c = s[i]
    for prev_c in list(prefix_count.keys()):
        pair = prev_c + c
        pair_count[pair] += prefix_count[prev_c]
        max_count = max(max_count, pair_count[pair])
    prefix_count[c] += 1

# Count three-character sequences with arithmetic progression
triple_count = defaultdict(int)
for i in range(n):
    for k in range(i + 2, n):
        if (i + k) % 2 == 0:
            j = (i + k) // 2
            triple = s[i] + s[j] + s[k]
            triple_count[triple] += 1
            max_count = max(max_count, triple_count[triple])

print(max_count)
