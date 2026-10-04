import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    m = data[1]
    
    edges = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        
        edges[u].append(v)
        edges[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    dp = [1] * (n + 1)
    answer = 0
    
    for v in range(1, n + 1):
        for u in edges[v]:
            if u < v:
                dp[v] = max(dp[v], dp[u] + 1)
        
        answer = max(answer, dp[v] * degree[v])
    
    print(answer)

if __name__ == "__main__":
    main()
