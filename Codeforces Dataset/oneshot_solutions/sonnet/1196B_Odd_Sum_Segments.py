def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Find positions of odd elements (0-indexed)
    odd_pos = [i for i in range(n) if a[i] % 2 == 1]
    
    # Check if solution is possible
    if len(odd_pos) < k or len(odd_pos) % 2 != k % 2:
        print("NO")
        return
    
    print("YES")
    # Output the ending positions (1-indexed) of each subsegment
    result = [odd_pos[i] + 1 for i in range(k - 1)]
    result.append(n)
    print(' '.join(map(str, result)))

q = int(input())
for _ in range(q):
    solve()
