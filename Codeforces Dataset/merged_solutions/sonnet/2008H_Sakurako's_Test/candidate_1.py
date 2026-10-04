# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = data[idx]
        q = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        queries = data[idx:idx + q]
        idx += q
        
        limit = n
        freq = [0] * (limit + 1)
        for v in a:
            freq[v] += 1
        
        prefix = [0] * (limit + 1)
        for i in range(1, limit + 1):
            prefix[i] = prefix[i - 1] + freq[i]
        
        need = (n + 2) // 2
        answers = {}
        
        for x in set(queries):
            low, high = 0, x - 1
            
            while low < high:
                mid = (low + high) // 2
                count = 0
                
                start = 0
                while start <= limit:
                    left = start
                    right = min(start + mid, limit)
                    if left <= right:
                        if left == 0:
                            count += prefix[right]
                        else:
                            count += prefix[right] - prefix[left - 1]
                    start += x
                
                if count >= need:
                    high = mid
                else:
                    low = mid + 1
            
            answers[x] = low
        
        out.append(' '.join(str(answers[x]) for x in queries))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
