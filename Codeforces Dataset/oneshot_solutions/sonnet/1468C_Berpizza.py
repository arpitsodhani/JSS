import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    idx = 1
    
    served = [False] * (q + 2)
    heap = []
    first_waiting = 1
    customer_id = 0
    answer = []
    
    for _ in range(q):
        query_type = int(data[idx])
        idx += 1
        
        if query_type == 1:
            money = int(data[idx])
            idx += 1
            customer_id += 1
            heapq.heappush(heap, (-money, customer_id))
        
        elif query_type == 2:
            while served[first_waiting]:
                first_waiting += 1
            
            served[first_waiting] = True
            answer.append(str(first_waiting))
        
        else:
            while served[heap[0][1]]:
                heapq.heappop(heap)
            
            _, chosen = heapq.heappop(heap)
            served[chosen] = True
            answer.append(str(chosen))
    
    print(' '.join(answer))

if __name__ == "__main__":
    main()
