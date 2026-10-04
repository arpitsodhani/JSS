import sys
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    # Count pairs for each sum
    sum_count = defaultdict(int)
    
    for i in range(n):
        for j in range(i+1, n):
            s = a[i] + a[j]
            sum_count[s] += 1
    
    # Return the maximum count
    print(max(sum_count.values()) if sum_count else 0)

main()
