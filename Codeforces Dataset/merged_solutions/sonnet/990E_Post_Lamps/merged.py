# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    n = data[idx]
    m = data[idx + 1]
    k = data[idx + 2]
    idx += 3
    
    blocked = [False] * n
    for _ in range(m):
        blocked[data[idx]] = True
        idx += 1
    
    cost = [0] + data[idx:idx + k]
    
    prev_free = [-1] * n
    last = -1
    for i in range(n):
        if not blocked[i]:
            last = i
        prev_free[i] = last
    
    if blocked[0]:
        print(-1)
        return
    
    answer = None
    
    for length in range(1, k + 1):
        lamps = 0
        covered = 0
        
        while covered < n:
            pos = prev_free[covered]
            if pos == -1 or pos + length <= covered:
                lamps = -1
                break
            
            lamps += 1
            covered = pos + length
        
        if lamps != -1:
            total = lamps * cost[length]
            if answer is None or total < answer:
                answer = total
    
    print(answer if answer is not None else -1)

if __name__ == "__main__":
    main()


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


