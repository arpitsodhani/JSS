import sys
import heapq

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        S = list(map(int, input().split()))
        
        heap = S[:]
        heapq.heapify(heap)
        in_set = set(S)
        
        score = 1
        
        for _ in range(k):
            # Get minimum, skipping any elements no longer in set
            while heap and heap[0] not in in_set:
                heapq.heappop(heap)
            
            if not heap:
                break
            
            m = heapq.heappop(heap)
            in_set.remove(m)
            score = (score * m) % MOD
            
            # Add 1..m-1 to the set (only those not already present)
            for i in range(1, m):
                if i not in in_set:
                    in_set.add(i)
                    heapq.heappush(heap, i)
        
        print(score)

if __name__ == "__main__":
    main()
