# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    idx = 1
    
    day = 0
    for _ in range(n):
        s = data[idx]
        d = data[idx + 1]
        idx += 2
        
        if s > day:
            day = s
        else:
            k = (day - s) // d + 1
            day = s + k * d
    
    print(day)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
