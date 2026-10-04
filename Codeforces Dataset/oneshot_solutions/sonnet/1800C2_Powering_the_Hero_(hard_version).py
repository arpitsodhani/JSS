import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        bonuses = []
        total = 0
        
        for _ in range(n):
            power = data[idx]
            idx += 1
            
            if power > 0:
                heapq.heappush(bonuses, -power)
            elif bonuses:
                total -= heapq.heappop(bonuses)
        
        answers.append(str(total))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
