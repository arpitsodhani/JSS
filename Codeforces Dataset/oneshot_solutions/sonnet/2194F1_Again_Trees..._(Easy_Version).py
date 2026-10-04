import sys

def main():
    sys.setrecursionlimit(300000)
    data = sys.stdin.buffer.read().decode('utf-8').split()
    idx = 0
    MOD = 10**9 + 7
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = [0] + [int(data[idx + i]) for i in range(n)]
        idx += n
        
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = int(data[idx]), int(data[idx + 1])
            idx += 2
            adj[u].append(v)
            adj[v].append(u)
        
        k = int(data[idx])
        idx += 1
        
        b = set(int(data[idx + i]) for i in range(k))
        idx += k
        
        dp = [{} for _ in range(n + 1)]
        
        def dfs(v, p):
            dp[v] = {a[v]: 1}
            
            for u in adj[v]:
                if u == p:
                    continue
                
                dfs(u, v)
                
                new_dp = {}
                for xv, cv in dp[v].items():
                    for xu, cu in dp[u].items():
                        w = cv * cu % MOD
                        
                        # Keep edge - combine XORs
                        x = xv ^ xu
                        new_dp[x] = (new_dp.get(x, 0) + w) % MOD
                        
                        # Remove edge - child component must have XOR in b
                        if xu in b:
                            new_dp[xv] = (new_dp.get(xv, 0) + w) % MOD
                
                dp[v] = new_dp
        
        dfs(1, 0)
        
        ans = sum(dp[1].get(x, 0) for x in b) % MOD
        print(ans)

if __name__ == "__main__":
    main()
