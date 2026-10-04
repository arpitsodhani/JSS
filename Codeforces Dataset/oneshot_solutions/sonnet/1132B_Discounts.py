import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx])
    idx += 1
    
    prices = []
    for _ in range(n):
        prices.append(int(data[idx]))
        idx += 1
    
    prices.sort()
    total = sum(prices)
    
    m = int(data[idx])
    idx += 1
    
    result = []
    for _ in range(m):
        q = int(data[idx])
        idx += 1
        result.append(str(total - prices[n - q]))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
