import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, k = data[0], data[1], data[2]
    a = data[3:]
    
    neg_inf = -10**30
    dp = [neg_inf] * m
    answer = 0
    
    for x in a:
        ndp = [neg_inf] * m
        
        ndp[1 % m] = max(ndp[1 % m], x - k)
        
        for rem in range(m):
            if dp[rem] == neg_inf:
                continue
            
            new_rem = (rem + 1) % m
            value = dp[rem] + x
            if rem == 0:
                value -= k
            
            if value > ndp[new_rem]:
                ndp[new_rem] = value
        
        dp = ndp
        best = max(dp)
        if best > answer:
            answer = best
    
    print(answer)

if __name__ == "__main__":
    main()
