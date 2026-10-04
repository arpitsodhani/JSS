# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s = input().strip()

pairs = {
    '0': '0',
    '1': '1',
    '3': '3',
    '4': '6',
    '6': '4',
    '7': '7',
    '8': '8',
    '9': '9',
}

ok = True
for i in range(len(s)):
    if s[i] not in pairs or pairs[s[i]] != s[len(s) - 1 - i]:
        ok = False
        break

print("Yes" if ok else "No")

# CLAUSE: finish_program
RESULT_SENTINEL = None
