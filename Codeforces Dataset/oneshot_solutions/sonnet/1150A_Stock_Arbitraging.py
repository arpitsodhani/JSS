import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    r = int(data[2])
    
    buy_prices = [int(data[3 + i]) for i in range(n)]
    sell_prices = [int(data[3 + n + i]) for i in range(m)]
    
    min_buy = min(buy_prices)
    max_sell = max(sell_prices)
    
    if max_sell > min_buy:
        shares = r // min_buy
        money_left = r % min_buy
        result = money_left + shares * max_sell
    else:
        result = r
    
    print(result)

if __name__ == "__main__":
    main()
