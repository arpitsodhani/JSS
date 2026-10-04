from collections import deque

n, k = map(int, input().split())
s = input().strip()

visited = set()
visited.add(s)
queue = deque([s])

count = 0
total_cost = 0

while queue and count < k:
    current = queue.popleft()
    count += 1
    total_cost += n - len(current)
    
    if count >= k:
        break
    
    # Generate all subsequences by removing one character
    for i in range(len(current)):
        new_subseq = current[:i] + current[i+1:]
        if new_subseq not in visited:
            visited.add(new_subseq)
            queue.append(new_subseq)

if count < k:
    print(-1)
else:
    print(total_cost)
