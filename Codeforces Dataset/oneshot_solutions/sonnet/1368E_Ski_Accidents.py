import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        edges = []
        for _ in range(m):
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            edges.append((u, v))
        
        depth = [0] * (n + 1)
        closed = [False] * (n + 1)
        result = []
        
        for u, v in edges:
            if closed[u] or closed[v]:
                continue
            
            depth[v] = max(depth[v], depth[u] + 1)
            if depth[v] == 2:
                closed[v] = True
                result.append(v)
        
        answers.append(str(len(result)))
        answers.append(' '.join(map(str, result)))
    
    sys.stdout.write('\n'.join(answers))

if __name__ == "__main__":
    main()
