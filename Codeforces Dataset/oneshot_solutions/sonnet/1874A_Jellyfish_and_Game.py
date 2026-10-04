def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Round 1: Jellyfish's turn
    min_a = min(a)
    max_b = max(b)
    if min_a < max_b:
        a[a.index(min_a)] = max_b
        b[b.index(max_b)] = min_a
    
    if k == 1:
        print(sum(a))
        return
    
    # Round 2: Gellyfish's turn
    min_b = min(b)
    max_a = max(a)
    if min_b < max_a:
        b[b.index(min_b)] = max_a
        a[a.index(max_a)] = min_b
    
    # For k >= 3 and k is odd, do one more Jellyfish move
    if k >= 3 and k % 2 == 1:
        min_a = min(a)
        max_b = max(b)
        if min_a < max_b:
            a[a.index(min_a)] = max_b
            b[b.index(max_b)] = min_a
    
    print(sum(a))

t = int(input())
for _ in range(t):
    solve()
