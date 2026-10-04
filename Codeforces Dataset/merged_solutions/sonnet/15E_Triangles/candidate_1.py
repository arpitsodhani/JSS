# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

MOD = 1000000009

def main():
    n = int(sys.stdin.readline())
    
    power = 2
    ways = 2
    add = 4
    
    for _ in range(n // 2 - 1):
        power = (power * 2) % MOD
        add = add * (power - 3) % MOD
        ways = (ways + add) % MOD
    
    answer = (2 * (ways * ways + 1)) % MOD
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
