# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import comb

def main():
    data = sys.stdin.read().split()
    target_commands = data[0]
    received_commands = data[1]
    
    target = target_commands.count('+') - target_commands.count('-')
    current = received_commands.count('+') - received_commands.count('-')
    unknown = received_commands.count('?')
    
    need = target - current
    
    if (need + unknown) % 2 != 0 or abs(need) > unknown:
        print("0.000000000000")
        return
    
    plus_needed = (need + unknown) // 2
    good = comb(unknown, plus_needed)
    total = 2 ** unknown
    
    print(f"{good / total:.12f}")

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
