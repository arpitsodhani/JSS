# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def solve_case(n, y, prices):
    max_price = max(prices)
    
    if max_price == 1:
        return n
    
    freq = [0] * (max_price + 1)
    for c in prices:
        freq[c] += 1
    
    prefix = [0] * (max_price + 1)
    for i in range(1, max_price + 1):
        prefix[i] = prefix[i - 1] + freq[i]
    
    best = -10**30
    
    for x in range(2, max_price + 1):
        total = 0
        reused = 0
        
        new_price = 1
        left = 1
        while left <= max_price:
            right = min(max_price, left + x - 1)
            count = prefix[right] - prefix[left - 1]
            
            if count:
                total += count * new_price
                if new_price <= max_price and freq[new_price]:
                    reused += min(freq[new_price], count)
            
            left += x
            new_price += 1
        
        best = max(best, total - y * (n - reused))
    
    return best

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        y = data[idx + 1]
        idx += 2
        
        prices = data[idx:idx + n]
        idx += n
        
        answers.append(str(solve_case(n, y, prices)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
