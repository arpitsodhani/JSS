import sys

def main():
    n, k, a, b = map(int, sys.stdin.read().split())
    
    if k == 1:
        print((n - 1) * a)
        return
    
    cost = 0
    
    while n > 1:
        if n < k:
            cost += (n - 1) * a
            break
        
        rem = n % k
        if rem:
            cost += rem * a
            n -= rem
        else:
            next_n = n // k
            subtract_cost = (n - next_n) * a
            cost += min(b, subtract_cost)
            n = next_n
    
    print(cost)

if __name__ == "__main__":
    main()
