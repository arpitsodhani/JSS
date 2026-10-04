import sys
from collections import Counter

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        if n < 3:
            print(0)
            idx += n
            continue
        
        a = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        freq = Counter(a)
        sorted_exponents = sorted(freq.keys())
        
        answer = 0
        cumsum = 0
        
        for exp in sorted_exponents:
            count = freq[exp]
            # Case 1: All three have the same exponent
            if count >= 3:
                answer += count * (count - 1) * (count - 2) // 6
            # Case 2: Two have this exponent, one has a smaller exponent
            if count >= 2:
                answer += count * (count - 1) // 2 * cumsum
            cumsum += count
        
        print(answer)

if __name__ == "__main__":
    main()
