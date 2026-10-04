# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:]
    
    a.sort()
    
    result = 0
    for i in range(n // 2):
        s = a[i] + a[n - 1 - i]
        result += s * s
    
    print(result)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
