import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        degree = [0] * (n + 1)
        edges = []
        
        for _ in range(n - 1):
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            
            edges.append((u, v))
            degree[u] += 1
            degree[v] += 1
        
        if n <= 2:
            answers.append("0")
            continue
        
        leaves = 0
        score = [0] * (n + 1)
        
        for v in range(1, n + 1):
            if degree[v] == 1:
                leaves += 1
                score[v] = 1
        
        for u, v in edges:
            if degree[u] == 1:
                score[v] += 1
            if degree[v] == 1:
                score[u] += 1
        
        answers.append(str(leaves - max(score)))
    
    print("\n".join(answers))

if __name__ == "__main__":
    main()
