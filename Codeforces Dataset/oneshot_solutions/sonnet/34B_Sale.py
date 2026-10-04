import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    prices = data[2:2 + n]
    
    prices.sort()
    
    earned = 0
    for i in range(min(n, m)):
        if prices[i] < 0:
            earned -= prices[i]
        else:
            break
    
    print(earned)

if __name__ == "__main__":
    main()
