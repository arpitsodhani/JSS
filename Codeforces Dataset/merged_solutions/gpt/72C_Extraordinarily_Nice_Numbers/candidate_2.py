# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s = input().strip()
n_mod_4 = int(s[-2:]) % 4 if len(s) >= 2 else int(s) % 4
print('yes' if n_mod_4 == 2 else 'no')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
