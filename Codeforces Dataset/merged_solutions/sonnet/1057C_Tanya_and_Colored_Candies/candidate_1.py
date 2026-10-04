# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    s = int(data[1]) - 1
    k = int(data[2])
    
    candies = list(map(int, data[3:3 + n]))
    colors = data[3 + n].strip()
    
    inf = 10 ** 18
    dp = [[inf] * (k + 1) for _ in range(n)]
    
    for i in range(n):
        got = min(k, candies[i])
        dp[i][got] = abs(i - s)
    
    order = sorted(range(n), key=lambda x: candies[x])
    
    for i in order:
        for j in order:
            if candies[j] >= candies[i]:
                break
            if colors[i] == colors[j]:
                continue
            
            dist = abs(i - j)
            add = candies[i]
            for eaten in range(k + 1):
                if dp[j][eaten] == inf:
                    continue
                new_eaten = min(k, eaten + add)
                cost = dp[j][eaten] + dist
                if cost < dp[i][new_eaten]:
                    dp[i][new_eaten] = cost
    
    answer = min(dp[i][k] for i in range(n))
    print(-1 if answer == inf else answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
