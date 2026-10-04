# CLAUSE: setup_environment
import sys
import re

# CLAUSE: solve_logic
s = sys.stdin.readline().strip()

allowed = re.compile(r'^[A-Za-z0-9_]+$')

def valid_part(x):
    return 1 <= len(x) <= 16 and allowed.fullmatch(x) is not None

def valid_host(h):
    if not (1 <= len(h) <= 32):
        return False
    parts = h.split('.')
    return all(valid_part(p) for p in parts)

ok = True

if s.count('@') != 1:
    ok = False
else:
    left, rest = s.split('@')
    if not valid_part(left):
        ok = False
    else:
        if rest.count('/') > 1:
            ok = False
        elif '/' in rest:
            host, res = rest.split('/')
            ok = valid_host(host) and valid_part(res)
        else:
            ok = valid_host(rest)

print("YES" if ok else "NO")

# CLAUSE: finish_program
RESULT_SENTINEL = None
