import sys

MOD = 1000000007

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    children = [[] for _ in range(n)]
    for v in range(1, n):
        p = data[idx]
        idx += 1
        children[p].append(v)
    
    color = data[idx:idx + n]
    
    order = [0]
    for v in order:
        order.extend(children[v])
    
    dp0 = [0] * n
    dp1 = [0] * n
    
    for v in reversed(order):
        if color[v] == 1:
            zero, one = 0, 1
        else:
            zero, one = 1, 0
        
        for c in children[v]:
            total = (dp0[c] + dp1[c]) % MOD
            new_zero = zero * total % MOD
            new_one = (one * total + zero * dp1[c]) % MOD
            zero, one = new_zero, new_one
        
        dp0[v] = zero
        dp1[v] = one
    
    print(dp1[0] % MOD)

if __name__ == "__main__":
    main()
