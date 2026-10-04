import sys

def main():
    data = sys.stdin.read().strip()
    tokens = data.split()
    len_val = int(tokens[0])
    k = int(tokens[1])
    a = [int(tokens[i]) for i in range(2, len(tokens))]
    n = len(a)
    
    max_optimal = 0
    
    for start in range(n - len_val + 1):
        interval = a[start:start + len_val]
        current_sum = sum(interval)
        
        # Try flipping the i smallest elements (to maximize positive sum)
        sorted_asc = sorted(interval)
        for num_flips in range(min(k, len_val) + 1):
            temp_sum = current_sum
            for i in range(num_flips):
                temp_sum -= 2 * sorted_asc[i]
            max_optimal = max(max_optimal, abs(temp_sum))
        
        # Try flipping the i largest elements (to maximize negative sum magnitude)
        sorted_desc = sorted(interval, reverse=True)
        for num_flips in range(min(k, len_val) + 1):
            temp_sum = current_sum
            for i in range(num_flips):
                temp_sum -= 2 * sorted_desc[i]
            max_optimal = max(max_optimal, abs(temp_sum))
    
    print(max_optimal)

if __name__ == "__main__":
    main()
