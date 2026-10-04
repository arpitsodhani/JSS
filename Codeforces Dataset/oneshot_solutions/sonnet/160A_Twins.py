import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    coins = data[1:1 + n]
    
    coins.sort(reverse=True)
    total = sum(coins)
    current = 0
    
    for i, coin in enumerate(coins, 1):
        current += coin
        if current > total - current:
            print(i)
            return

if __name__ == "__main__":
    main()
