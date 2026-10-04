import sys

MOD = 1000000007

def main():
    x = sys.stdin.readline().strip()
    n = len(x)
    
    result = 0
    power = pow(2, n - 1, MOD)
    
    for ch in reversed(x):
        if ch == '1':
            result = (result + power) % MOD
        power = (power * 2) % MOD
    
    print(result)

if __name__ == "__main__":
    main()
