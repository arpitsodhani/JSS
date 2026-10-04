import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solve():
    n = int(input())
    b = list(map(int, input().split()))
    
    x = 1
    for i in range(n - 1):
        if b[i+1] % b[i] != 0:
            g = math.gcd(b[i], b[i+1])
            p = b[i] // g
            x = lcm(x, p)
    
    if x == 1:
        x = 2
    
    print(x)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
