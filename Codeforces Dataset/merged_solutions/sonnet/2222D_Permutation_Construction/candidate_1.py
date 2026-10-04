# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + a[i - 1]
        
        order = sorted(range(n), key=lambda i: (prefix[i], i))
        p = [0] * n
        
        value = n
        for pos in order:
            p[pos] = value
            value -= 1
        
        out.append(' '.join(map(str, p)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
