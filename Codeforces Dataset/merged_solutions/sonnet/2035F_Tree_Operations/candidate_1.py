# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        x = data[idx + 1]
        idx += 2
        
        a = [0] + data[idx:idx + n]
        idx += n
        
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        
        parent = [0] * (n + 1)
        order = [x]
        parent[x] = -1
        
        for v in order:
            for to in graph[v]:
                if to != parent[v]:
                    parent[to] = v
                    order.append(to)
        
        size = [1] * (n + 1)
        subtree_sum = a[:]
        
        for v in reversed(order):
            for to in graph[v]:
                if parent[to] == v:
                    size[v] += size[to]
                    subtree_sum[v] += subtree_sum[to]
        
        total_sum = subtree_sum[x]
        parity = total_sum & 1
        
        def possible(operations):
            if operations < total_sum or ((operations - total_sum) & 1):
                return False
            
            q, r = divmod(operations, n)
            
            pref = [0] * (n + 1)
            for i in range(1, r + 1):
                pref[i] = 1
            
            for v in reversed(order):
                p = parent[v]
                if p != -1:
                    pref[p] += pref[v]
            
            need = [0] * (n + 1)
            
            for v in reversed(order):
                child_need = 0
                for to in graph[v]:
                    if parent[to] == v:
                        child_need += need[to]
                
                forced = q * size[v] + pref[v]
                cur = max(child_need, forced - subtree_sum[v], 0)
                if cur & 1:
                    cur += 1
                need[v] = cur
            
            root_child_need = 0
            for to in graph[x]:
                if parent[to] == x:
                    root_child_need += need[to]
            
            return operations - total_sum >= root_child_need
        
        high = parity
        while high < total_sum:
            high += 2
        
        while not possible(high):
            high = high * 2 + 2
        
        low = parity - 2
        while high - low > 2:
            mid = ((low + high) // 4) * 2 + parity
            if mid <= low:
                mid += 2
            
            if possible(mid):
                high = mid
            else:
                low = mid
        
        answers.append(str(high))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
