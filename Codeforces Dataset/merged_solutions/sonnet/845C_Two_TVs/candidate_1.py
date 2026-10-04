# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    events = []
    idx = 1
    
    for _ in range(n):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        events.append((l, 1))
        events.append((r, -1))
    
    events.sort(key=lambda x: (x[0], -x[1]))
    
    active = 0
    for _, kind in events:
        active += kind
        if active > 2:
            print("NO")
            return
    
    print("YES")

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
