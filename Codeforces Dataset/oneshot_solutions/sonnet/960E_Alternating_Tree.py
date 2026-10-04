import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    V = [0] + [int(input_data[idx + i]) for i in range(n)]
    idx += n
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    MOD = 10**9 + 7
    
    down_sum = [0] * (n + 1)
    down_cnt = [0] * (n + 1)
    
    def dfs_down(u, parent):
        down_sum[u] = V[u]
        down_cnt[u] = 1
        for c in adj[u]:
            if c == parent:
                continue
            dfs_down(c, u)
            down_sum[u] += down_cnt[c] * V[u] - down_sum[c]
            down_cnt[u] += down_cnt[c]
    
    dfs_down(1, 0)
    
    total_sum = [0] * (n + 1)
    
    def dfs_up(u, parent, up_sum):
        total_sum[u] = down_sum[u] + up_sum
        for c in adj[u]:
            if c == parent:
                continue
            up_sum_c = (n - down_cnt[c]) * V[c] - total_sum[u] + down_cnt[c] * V[u] - down_sum[c]
            dfs_up(c, u, up_sum_c)
    
    dfs_up(1, 0, 0)
    
    answer = sum(total_sum[1:]) % MOD
    print(answer)

if __name__ == "__main__":
    main()
