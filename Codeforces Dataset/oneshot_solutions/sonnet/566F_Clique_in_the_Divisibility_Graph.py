import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    numbers = data[1:]
    
    if len(numbers) != n:
        numbers = data
    
    max_value = max(numbers)
    count = [0] * (max_value + 1)
    for x in numbers:
        count[x] += 1
    
    dp = [0] * (max_value + 1)
    answer = 0
    
    for x in range(1, max_value + 1):
        if count[x]:
            dp[x] += count[x]
            if dp[x] > answer:
                answer = dp[x]
        
        if dp[x]:
            for multiple in range(x + x, max_value + 1, x):
                if count[multiple] and dp[x] > dp[multiple]:
                    dp[multiple] = dp[x]
    
    print(answer)

if __name__ == "__main__":
    main()
