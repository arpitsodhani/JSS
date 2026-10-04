# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def ask(x, y):
    print(1, x, y, flush=True)
    ans = sys.stdin.readline().strip()
    return ans == "TAK"

def find_point(l, r):
    while l < r:
        mid = (l + r) // 2
        if ask(mid, mid + 1):
            r = mid
        else:
            l = mid + 1
    return l

def is_chosen(x, known):
    return ask(x, known)

def main():
    line = sys.stdin.readline().split()
    if not line:
        return
    
    n, k = map(int, line)
    
    first = find_point(1, n)
    second = -1
    
    if first > 1:
        candidate = find_point(1, first - 1)
        if is_chosen(candidate, first):
            second = candidate
    
    if second == -1 and first < n:
        second = find_point(first + 1, n)
    
    print(2, first, second, flush=True)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
