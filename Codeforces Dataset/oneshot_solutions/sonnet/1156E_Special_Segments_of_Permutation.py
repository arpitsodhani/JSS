import sys
sys.setrecursionlimit(300000)

def solve():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    
    def count_special(l, r):
        if l >= r:
            return 0
        
        # Find position of maximum
        max_pos = l
        for i in range(l + 1, r + 1):
            if p[i] > p[max_pos]:
                max_pos = i
        
        max_val = p[max_pos]
        count = 0
        
        # Extend from max_pos while elements < max_val
        left_bound = max_pos
        while left_bound > l and p[left_bound - 1] < max_val:
            left_bound -= 1
        
        right_bound = max_pos
        while right_bound < r and p[right_bound + 1] < max_val:
            right_bound += 1
        
        # Count subsegments where p[l'] + p[r'] = max_val
        right_values = {}
        for i in range(max_pos, right_bound + 1):
            if p[i] not in right_values:
                right_values[p[i]] = 0
            right_values[p[i]] += 1
        
        for i in range(left_bound, max_pos + 1):
            needed = max_val - p[i]
            if needed in right_values:
                count += right_values[needed]
        
        # Recurse on left and right parts
        count += count_special(l, max_pos - 1)
        count += count_special(max_pos + 1, r)
        
        return count
    
    print(count_special(0, n - 1))

solve()
