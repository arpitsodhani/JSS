# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from heapq import heappush, heappop

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    inf = 10 ** 30
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        values = []
        initial = []
        operations = []
        
        for _ in range(n):
            x = int(data[idx])
            idx += 1
            initial.append(x)
            values.append(x)
        
        for _ in range(m):
            op = data[idx].decode()
            x = int(data[idx + 1])
            idx += 2
            operations.append((op, x))
            if op != '?':
                values.append(x)
        
        values.append(0)
        values = sorted(set(values))
        comp = {x: i for i, x in enumerate(values)}
        size = len(values)
        
        left = [-1] * size
        right = [-1] * size
        active = [False] * size
        heap = []
        
        def add_gap(a, b):
            if b == -1:
                length = inf
            else:
                length = values[b] - values[a] - 1
            if length > 0:
                heappush(heap, (-(length), a, b))
        
        present = sorted(set(initial))
        order = [0] + present
        
        for i, x in enumerate(order):
            c = comp[x]
            active[c] = True
            if i > 0:
                p = comp[order[i - 1]]
                left[c] = p
                right[p] = c
        
        for i, x in enumerate(order):
            c = comp[x]
            add_gap(c, right[c])
        
        def insert_value(x):
            c = comp[x]
            if active[c]:
                return
            
            pos = c - 1
            while pos >= 0 and not active[pos]:
                pos -= 1
            
            nxt = right[pos]
            active[c] = True
            left[c] = pos
            right[c] = nxt
            right[pos] = c
            if nxt != -1:
                left[nxt] = c
            
            add_gap(pos, c)
            add_gap(c, nxt)
        
        def remove_value(x):
            c = comp[x]
            if not active[c]:
                return
            
            p = left[c]
            nxt = right[c]
            active[c] = False
            right[p] = nxt
            if nxt != -1:
                left[nxt] = p
            
            add_gap(p, nxt)
        
        def query(k):
            while heap:
                neg_len, a, b = heap[0]
                if not active[a] or right[a] != b:
                    heappop(heap)
                    continue
                
                length = -neg_len
                if b != -1:
                    real = values[b] - values[a] - 1
                else:
                    real = inf
                
                if real != length:
                    heappop(heap)
                    continue
                
                if length >= k:
                    return values[a] + 1
                
                break
            
            return values[0] + 1
        
        for op, x in operations:
            if op == '+':
                insert_value(x)
            elif op == '-':
                remove_value(x)
            else:
                out.append(str(query(x)))
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
