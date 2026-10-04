import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        m = data[idx]
        x = data[idx + 1]
        idx += 2
        
        total = 0
        chosen = []
        
        for month in range(m):
            cost = data[idx]
            idx += 1
            
            budget = month * x
            
            if total + cost <= budget:
                total += cost
                heapq.heappush(chosen, -cost)
            elif chosen and -chosen[0] > cost:
                total += cost + heapq.heappop(chosen)
                heapq.heappush(chosen, -cost)
        
        answers.append(str(len(chosen)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
