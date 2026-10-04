def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Create pairs and sort them
    pairs = [(a[i], b[i], i) for i in range(n)]
    sorted_pairs = sorted(pairs, key=lambda x: (x[0], x[1]))
    
    # Check if b values are also sorted after sorting pairs
    for i in range(1, n):
        if sorted_pairs[i][1] < sorted_pairs[i-1][1]:
            print(-1)
            return
    
    # Get target sorted arrays
    target_a = [sorted_pairs[i][0] for i in range(n)]
    target_b = [sorted_pairs[i][1] for i in range(n)]
    
    # Work with copies of the arrays
    curr_a = a[:]
    curr_b = b[:]
    
    moves = []
    
    # Use selection sort to find swaps
    for i in range(n):
        # Find where the target pair currently is
        for j in range(i, n):
            if curr_a[j] == target_a[i] and curr_b[j] == target_b[i]:
                if i != j:
                    # Swap positions i and j
                    curr_a[i], curr_a[j] = curr_a[j], curr_a[i]
                    curr_b[i], curr_b[j] = curr_b[j], curr_b[i]
                    moves.append((i+1, j+1))  # 1-indexed
                break
    
    print(len(moves))
    for move in moves:
        print(move[0], move[1])

t = int(input())
for _ in range(t):
    solve()
