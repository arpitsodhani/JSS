# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    initial = int(input())
    
    B = 10
    S = 1010
    
    # Phase 1: Make B small forward steps
    forward_positions = {initial: 0}
    current = initial
    for i in range(1, B + 1):
        print("+ 1", flush=True)
        current = int(input())
        if current == initial:
            # Found cycle in phase 1
            print(f"! {i}", flush=True)
            return
        if current not in forward_positions:
            forward_positions[current] = i
    
    # Phase 2: Make large backward steps
    for k in range(1, 991):
        print(f"- {S}", flush=True)
        current = int(input())
        if current in forward_positions:
            i = forward_positions[current]
            n = i + k * S - B
            if n > 0:
                print(f"! {n}", flush=True)
                return

solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
