# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n = data[0]
    a = data[1:1 + n]
    
    seen = [False] * (n + 1)
    change = [False] * n
    
    for i, x in enumerate(a):
        if 1 <= x <= n and not seen[x]:
            seen[x] = True
        else:
            change[i] = True
    
    missing = [i for i in range(1, n + 1) if not seen[i]]
    ptr = 0
    
    for i in range(n):
        if change[i]:
            a[i] = missing[ptr]
            ptr += 1
    
    print(' '.join(map(str, a)))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
