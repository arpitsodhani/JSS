import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    b = data[1]
    idx = 2
    
    queue = deque()
    answer = []
    
    for _ in range(n):
        t = data[idx]
        d = data[idx + 1]
        idx += 2
        
        while queue and queue[0] <= t:
            queue.popleft()
        
        if len(queue) > b:
            answer.append(-1)
            continue
        
        start = t if not queue else queue[-1]
        finish = start + d
        queue.append(finish)
        answer.append(finish)
    
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    main()
