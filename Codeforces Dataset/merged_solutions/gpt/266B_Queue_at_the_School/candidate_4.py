# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n, t = map(int, input().split())
    s = list(input().strip())

    for _ in range(t):
        i = 0
        while i < n - 1:
            if s[i] == 'B' and s[i + 1] == 'G':
                s[i], s[i + 1] = s[i + 1], s[i]
                i += 2
            else:
                i += 1

    print(''.join(s))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
