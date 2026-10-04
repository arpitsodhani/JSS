import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    last = [[0] * (n + 1) for _ in range(26)]
    
    for i, ch in enumerate(s, 1):
        c = ord(ch) - ord('a')
        for length in range(i, 0, -1):
            add = dp[length - 1]
            dp[length] += add - last[c][length]
            last[c][length] = add
    
    remaining = k
    answer = 0
    
    for length in range(n, -1, -1):
        take = min(remaining, dp[length])
        answer += take * (n - length)
        remaining -= take
        
        if remaining == 0:
            print(answer)
            return
    
    print(-1)

if __name__ == "__main__":
    main()
