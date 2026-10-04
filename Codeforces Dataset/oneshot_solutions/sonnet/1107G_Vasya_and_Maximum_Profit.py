import sys

def main():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(data[idx])
    a = int(data[idx + 1])
    idx += 2
    
    d = [0] * n
    c = [0] * n
    for i in range(n):
        d[i] = int(data[idx])
        c[i] = int(data[idx + 1])
        idx += 2
    
    max_profit = 0
    
    for l in range(n):
        cost_sum = 0
        max_gap = 0
        for r in range(l, n):
            cost_sum += c[r]
            if r > l:
                diff = d[r] - d[r - 1]
                gap = diff * diff
                if gap > max_gap:
                    max_gap = gap
            
            profit = a * (r - l + 1) - cost_sum - max_gap
            if profit > max_profit:
                max_profit = profit
    
    print(max_profit)

if __name__ == "__main__":
    main()
