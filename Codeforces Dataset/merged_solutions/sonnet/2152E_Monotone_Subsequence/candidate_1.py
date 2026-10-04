# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def solve():
    n = int(input())
    total = n * n + 1
    
    # Query rows of n+1 consecutive positions
    result = []
    for row in range(n):
        start = row * (n + 1) + 1
        end = min(start + n, total)
        if start > total:
            break
        group = list(range(start, end + 1))
        
        print("?", len(group), *group, flush=True)
        
        response = list(map(int, input().split()))
        m = response[0]
        visible = response[1:m+1] if m > 0 else []
        
        # If we found n+1 increasing elements, we're done
        if len(visible) >= n + 1:
            print("!", *visible[:n+1], flush=True)
            return
        
        result.append((group, set(visible)))
    
    # Build decreasing subsequence from non-visible positions by column
    columns = [[] for _ in range(n + 1)]
    for group, visible_set in result:
        for j, pos in enumerate(group):
            if pos not in visible_set:
                columns[j].append(pos)
    
    # Find a column with n+1 non-visible positions (forms decreasing subsequence)
    for col in columns:
        if len(col) >= n + 1:
            print("!", *col[:n+1], flush=True)
            return
    
    # Fallback (shouldn't reach here by Erdős–Szekeres theorem)
    print("!", *list(range(1, n + 2)), flush=True)

solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
