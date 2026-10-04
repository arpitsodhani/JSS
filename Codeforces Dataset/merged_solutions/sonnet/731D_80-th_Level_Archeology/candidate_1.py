# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    c = data[idx + 1]
    idx += 2
    
    words = []
    for _ in range(n):
        length = data[idx]
        idx += 1
        words.append(data[idx:idx + length])
        idx += length
    
    diff = [0] * (c + 1)
    
    for i in range(n - 1):
        a = words[i]
        b = words[i + 1]
        
        pos = 0
        limit = min(len(a), len(b))
        while pos < limit and a[pos] == b[pos]:
            pos += 1
        
        if pos == limit:
            if len(a) > len(b):
                print(-1)
                return
            continue
        
        x = a[pos] - 1
        y = b[pos] - 1
        
        if x < y:
            left = c - y
            right = c - x - 1
            diff[left] += 1
            diff[right + 1] -= 1
        else:
            left = c - x
            right = c - y - 1
            
            if left > 0:
                diff[0] += 1
                diff[left] -= 1
            if right + 1 < c:
                diff[right + 1] += 1
                diff[c] -= 1
    
    bad = 0
    for shift in range(c):
        bad += diff[shift]
        if bad == 0:
            print(shift)
            return
    
    print(-1)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
