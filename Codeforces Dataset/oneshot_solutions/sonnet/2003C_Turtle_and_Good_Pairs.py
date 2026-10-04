import sys
from collections import Counter

def solve(s):
    freq = Counter(s)
    result = []
    
    while freq:
        # Sort by frequency (descending), then lexicographically
        sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        
        # Pick the most frequent char different from the last
        chosen = None
        for char, _ in sorted_chars:
            if not result or char != result[-1]:
                chosen = char
                break
        
        # If all remaining chars are same as last, pick most frequent anyway
        if chosen is None:
            chosen = sorted_chars[0][0]
        
        result.append(chosen)
        freq[chosen] -= 1
        if freq[chosen] == 0:
            del freq[chosen]
    
    return ''.join(result)

# Read input
lines = sys.stdin.read().strip().split('\n')
t = int(lines[0])
idx = 1

for _ in range(t):
    n = int(lines[idx])
    s = lines[idx + 1]
    idx += 2
    print(solve(s))
