import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    
    # Number of colors needed
    num_colors = (n + k - 1) // k
    
    # Generate colors for all edges (i, j) where i < j
    colors = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Color based on which block j belongs to
            color = (j + k - 1) // k
            colors.append(str(color))
    
    print(num_colors)
    print(' '.join(colors))

solve()
