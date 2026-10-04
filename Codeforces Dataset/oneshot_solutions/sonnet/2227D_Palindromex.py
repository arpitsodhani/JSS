import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    max_mex = 0
    
    # Try all subarrays
    for l in range(2*n):
        for r in range(l, 2*n):
            # Check if subarray a[l:r+1] is palindrome
            is_palindrome = True
            left, right = l, r
            while left < right:
                if a[left] != a[right]:
                    is_palindrome = False
                    break
                left += 1
                right -= 1
            
            if is_palindrome:
                # Calculate MEX
                s = set(a[l:r+1])
                mex = 0
                while mex in s:
                    mex += 1
                max_mex = max(max_mex, mex)
                
                # Early exit if we found the maximum possible MEX
                if max_mex == n:
                    return max_mex
    
    return max_mex

t = int(input())
for _ in range(t):
    print(solve())
