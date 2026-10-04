# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    n, p = map(int, input().split())
    s = list(input().strip())

    for i in range(n - p):
        if s[i] != '.' and s[i + p] != '.' and s[i] != s[i + p]:
            print(''.join('0' if c == '.' else c for c in s))
            exit()

    for i in range(n - p):
        if s[i] == '.' or s[i + p] == '.':
            if s[i] == '.' and s[i + p] == '.':
                s[i] = '0'
                s[i + p] = '1'
            elif s[i] == '.':
                s[i] = '1' if s[i + p] == '0' else '0'
            else:
                s[i + p] = '1' if s[i] == '0' else '0'
            print(''.join('0' if c == '.' else c for c in s))
            exit()

    print("No")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
