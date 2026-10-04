# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n = data[0]
    s = data[1:1 + n]
    
    order = sorted(range(n), key=lambda i: s[i])
    
    a = [0] * n
    b = [0] * n
    
    for rank, i in enumerate(order):
        if s[i] < rank:
            print("NO")
            return
        a[i] = rank
        b[i] = s[i] - rank
    
    seen = set()
    for i in order:
        if b[i] in seen:
            print("NO")
            return
        seen.add(b[i])
    
    print("YES")
    print(" ".join(map(str, a)))
    print(" ".join(map(str, b)))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
