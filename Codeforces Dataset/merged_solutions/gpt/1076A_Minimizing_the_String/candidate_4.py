# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n = int(input())
    s = input().strip()

    pos = n - 1
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            pos = i
            break

    print(s[:pos] + s[pos + 1:])

# CLAUSE: finish_program
def main():
    _inner_main()

main()
