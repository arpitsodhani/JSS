# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    k = data[1]
    a = data[2:2 + n]
    b = data[2 + n:2 + 2 * n]
    
    available = []
    result = 0
    
    for i in range(n):
        heapq.heappush(available, a[i])
        best_prepare = heapq.heappop(available)
        
        heapq.heappush(available, b[i] + best_prepare)
    
    for _ in range(k):
        result += heapq.heappop(available)
    
    print(result)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
