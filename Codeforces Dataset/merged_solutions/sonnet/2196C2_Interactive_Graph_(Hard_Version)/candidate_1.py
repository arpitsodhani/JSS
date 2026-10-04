# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

sys.setrecursionlimit(300000)

def main():
    def ask(k):
        if k in cache:
            return cache[k]
        
        print("?", k, flush=True)
        
        line = sys.stdin.readline()
        while line is not None and line.strip() == "":
            line = sys.stdin.readline()
        
        if not line:
            return []
        
        values = list(map(int, line.split()))
        if values[0] == 0:
            path = []
        else:
            path = values[1:]
        
        cache[k] = path
        return path
    
    def add_edge(u, v):
        if (u, v) in edges:
            return
        
        edges.add((u, v))
        
        left = []
        right = []
        for a in range(1, n + 1):
            if a == u or reach[a][u]:
                left.append(a)
        for b in range(1, n + 1):
            if b == v or reach[v][b]:
                right.append(b)
        
        for a in left:
            row = reach[a]
            for b in right:
                row[b] = True
    
    def has_possible_next(v, last_child):
        for x in range(last_child + 1, n + 1):
            if x != v and not reach[x][v]:
                return True
        return False
    
    def starts_with(path, prefix):
        return len(path) >= len(prefix) and path[:len(prefix)] == prefix
    
    def explore(prefix, pos):
        v = prefix[-1]
        if done[v]:
            return path_count[v]
        
        total = 1
        next_pos = pos + 1
        last_child = 0
        
        while has_possible_next(v, last_child):
            path = ask(next_pos)
            
            if not starts_with(path, prefix):
                path_count[v] = next_pos - pos
                done[v] = True
                return path_count[v]
            
            child = path[len(prefix)]
            add_edge(v, child)
            
            if done[child]:
                child_count = path_count[child]
            else:
                child_count = explore(path, next_pos)
            
            total += child_count
            next_pos += child_count
            last_child = child
        
        path_count[v] = total
        done[v] = True
        return total
    
    first = sys.stdin.readline()
    while first.strip() == "":
        first = sys.stdin.readline()
    
    t = int(first)
    
    for _ in range(t):
        line = sys.stdin.readline()
        while line.strip() == "":
            line = sys.stdin.readline()
        
        n = int(line)
        
        cache = {}
        done = [False] * (n + 1)
        path_count = [0] * (n + 1)
        reach = [[False] * (n + 1) for _ in range(n + 1)]
        edges = set()
        
        pos = 1
        for v in range(1, n + 1):
            if done[v]:
                pos += path_count[v]
                continue
            
            path = ask(pos)
            if not path:
                break
            
            explore(path, pos)
            pos += path_count[v]
        
        print("!", len(edges), flush=True)
        for u, v in edges:
            print(u, v, flush=True)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
