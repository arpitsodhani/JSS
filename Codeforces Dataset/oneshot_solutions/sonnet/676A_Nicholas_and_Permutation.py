import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    # Find positions of 1 and n (0-indexed)
    pos1 = a.index(1)
    posn = a.index(n)
    
    # Calculate maximum distance after one swap
    # We can move 1 to position 0 or n-1, or move n to position 0 or n-1
    result = max(posn, n-1-posn, pos1, n-1-pos1)
    print(result)

solve()
