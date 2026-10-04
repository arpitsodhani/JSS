import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    a = list(map(int, input_data[idx:idx+n]))
    
    if n < 4:
        print("NO")
        return
    
    # Count occurrences and store indices
    value_indices = defaultdict(list)
    for i in range(n):
        value_indices[a[i]].append(i)
    
    # Check if any value appears 4+ times
    for indices in value_indices.values():
        if len(indices) >= 4:
            print("YES")
            print(indices[0]+1, indices[1]+1, indices[2]+1, indices[3]+1)
            return
    
    # Check if there are two values each appearing 2+ times
    pairs = []
    for indices in value_indices.values():
        if len(indices) >= 2:
            pairs.append(indices)
            if len(pairs) == 2:
                print("YES")
                print(pairs[0][0]+1, pairs[1][0]+1, pairs[0][1]+1, pairs[1][1]+1)
                return
    
    # Fall back to hash map approach
    sum_map = {}
    for i in range(n):
        for j in range(i+1, n):
            s = a[i] + a[j]
            if s in sum_map:
                for k, l in sum_map[s]:
                    if i != k and i != l and j != k and j != l:
                        print("YES")
                        print(i+1, j+1, k+1, l+1)
                        return
            
            if s not in sum_map:
                sum_map[s] = []
            sum_map[s].append((i, j))
    
    print("NO")

solve()
