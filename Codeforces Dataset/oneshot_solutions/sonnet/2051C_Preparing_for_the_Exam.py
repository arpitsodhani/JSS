t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    q_line = input()
    q = list(map(int, q_line.split())) if q_line.strip() else []
    
    known_set = set(q)
    num_known = len(known_set)
    
    if num_known == n:
        # Knows all questions - passes all lists
        print('1' * m)
    elif num_known == n - 1:
        # Knows exactly n-1 questions - find which one is missing
        all_sum = n * (n + 1) // 2
        known_sum = sum(known_set)
        missing = all_sum - known_sum
        
        # Pass only lists that are also missing this question
        result = ''.join('1' if ai == missing else '0' for ai in a)
        print(result)
    else:
        # Knows fewer than n-1 questions - fails all lists
        print('0' * m)
