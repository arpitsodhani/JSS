import sys
from collections import defaultdict

MOD = 10 ** 9 + 7

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        colors = [0] + data[idx:idx + n]
        idx += n
        
        dp = [0] * (n + 1)
        ways = [0] * (n + 1)
        ways[0] = 1
        
        positions = defaultdict(list)
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            ways[i] = ways[i - 1]
            
            color = colors[i]
            positions[color].append(i)
            pos = positions[color]
            
            if len(pos) >= k:
                first = pos[-k]
                candidate = dp[first - 1] + 1
                
                if candidate > dp[i]:
                    dp[i] = candidate
                    ways[i] = ways[first - 1]
                elif candidate == dp[i]:
                    ways[i] = (ways[i] + ways[first - 1]) % MOD
        
        answers.append(str(ways[n] % MOD))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
