import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    k = int(input_data[1])
    arr = [int(input_data[i]) for i in range(2, 2 + n)]
    
    # Sort array to process most negative first
    arr.sort()
    
    # Flip negative numbers starting from most negative
    for i in range(n):
        if k > 0 and arr[i] < 0:
            arr[i] = -arr[i]
            k -= 1
    
    # If k is still positive and odd, flip the smallest absolute value
    if k % 2 == 1:
        # Find the smallest absolute value
        min_idx = 0
        for i in range(1, n):
            if abs(arr[i]) < abs(arr[min_idx]):
                min_idx = i
        arr[min_idx] = -arr[min_idx]
    
    print(sum(arr))

solve()
