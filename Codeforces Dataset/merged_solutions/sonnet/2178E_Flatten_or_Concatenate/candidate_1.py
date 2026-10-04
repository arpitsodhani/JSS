# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

n = int(input())

def query(l, r):
    print(f"? {l} {r}")
    sys.stdout.flush()
    return int(input())

def find_max(l, r):
    if l > r:
        return 0
    if l == r:
        return query(l, l)
    mid = (l + r) // 2
    return max(find_max(l, mid), find_max(mid + 1, r))

max_val = find_max(1, n)
print(f"! {max_val}")
sys.stdout.flush()

# CLAUSE: finish_program
RESULT_SENTINEL = None
