# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        
        parent = [0] * (n + 1)
        stack = [n]
        parent[n] = -1
        order = []
        
        while stack:
            v = stack.pop()
            order.append(v)
            for u in graph[v]:
                if u != parent[v]:
                    parent[u] = v
                    stack.append(u)
        
        path_set = set()
        v = 1
        while v != -1:
            path_set.add(v)
            if v == n:
                break
            v = parent[v]
        
        bad = []
        for v in order:
            if v not in path_set:
                bad.append(v)
        
        answer = []
        for v in bad:
            answer.append((2, v))
            answer.append((1, 0))
        
        v = 1
        while v != n:
            answer.append((2, v))
            answer.append((1, 0))
            v = parent[v]
        
        while answer and answer[-1][0] == 2:
            answer.pop()
        
        out.append(str(len(answer)))
        for typ, val in answer:
            if typ == 1:
                out.append("1")
            else:
                out.append(f"2 {val}")
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
