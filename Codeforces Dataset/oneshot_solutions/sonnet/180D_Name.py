import sys
from collections import Counter

def solve(s, t):
    available = Counter(s)
    
    # Try to match t[0:split_point] then exceed at split_point
    # Try from right to left to get lexicographically smallest result
    for split_point in range(len(t), -1, -1):
        temp_available = available.copy()
        result = []
        
        # Try to match first split_point characters of t
        valid = True
        for i in range(split_point):
            if temp_available[t[i]] > 0:
                result.append(t[i])
                temp_available[t[i]] -= 1
            else:
                valid = False
                break
        
        if not valid:
            continue
        
        if split_point < len(t):
            # Need to exceed at position split_point
            found = False
            for c in sorted(temp_available.keys()):
                if c > t[split_point] and temp_available[c] > 0:
                    result.append(c)
                    temp_available[c] -= 1
                    found = True
                    break
            
            if not found:
                continue
            
            # Fill rest with smallest available characters
            for char in sorted(temp_available.elements()):
                result.append(char)
            
            return ''.join(result)
        else:
            # Matched all of t, need leftover characters
            if sum(temp_available.values()) > 0:
                for char in sorted(temp_available.elements()):
                    result.append(char)
                return ''.join(result)
    
    return "-1"

# Read input
lines = sys.stdin.read().strip().split('\n')
s = lines[0]
t = lines[1]

# Solve and print
print(solve(s, t))
