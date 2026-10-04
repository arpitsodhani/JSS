import sys

MOD = 998244353

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        dp1, dp2, dp3 = 0, 0, 0
        
        for i in range(n):
            if a[i] == 1:
                dp1 = (dp1 + 1) % MOD
            elif a[i] == 2:
                dp2 = (2 * dp2 + dp1) % MOD
            elif a[i] == 3:
                dp3 = (dp3 + dp2) % MOD
        
        results.append(dp3)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
