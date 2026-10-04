# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    if len(data) == 1:
        s = data[0]
    else:
        s = data[1]
    
    n = len(s)
    digits = [int(c) for c in s]
    
    for first_end in range(n - 1):
        target = sum(digits[:first_end + 1])
        current = 0
        parts = 1
        ok = True
        
        for i in range(first_end + 1, n):
            current += digits[i]
            if current == target:
                parts += 1
                current = 0
            elif current > target:
                ok = False
                break
        
        if ok and current == 0 and parts >= 2:
            print("YES")
            return
    
    print("NO")

main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
