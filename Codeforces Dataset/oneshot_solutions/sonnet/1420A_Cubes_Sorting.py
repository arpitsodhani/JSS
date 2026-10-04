import sys

input_data = sys.stdin.read().split()
idx = 0
t = int(input_data[idx])
idx += 1

for _ in range(t):
    n = int(input_data[idx])
    idx += 1
    a = [int(input_data[idx+i]) for i in range(n)]
    idx += n
    
    # Check if array is strictly descending
    strictly_descending = True
    for i in range(n-1):
        if a[i] <= a[i+1]:
            strictly_descending = False
            break
    
    print("NO" if strictly_descending else "YES")
