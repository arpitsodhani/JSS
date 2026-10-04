# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    t = int(input())
    for _ in range(t):
        x = list(map(int, input().split()))
        print(max(x) - min(x))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
