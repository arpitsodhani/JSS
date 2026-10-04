# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s = input().strip()
vowels = set('aoyeui')
result = []
for ch in s.lower():
    if ch not in vowels:
        result.append('.' + ch)
print(''.join(result))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
