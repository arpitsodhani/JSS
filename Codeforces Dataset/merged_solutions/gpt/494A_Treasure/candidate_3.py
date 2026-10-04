# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    s = sys.stdin.readline().strip()

    cnt_hash = s.count('#')
    if cnt_hash == 0:
        print(-1)
        sys.exit()

    opens = s.count('(')
    closes = s.count(')')
    last_value = opens - closes - (cnt_hash - 1)

    ans = [1] * cnt_hash
    ans[-1] = last_value

    if last_value < 1:
        print(-1)
        sys.exit()

    balance = 0
    idx = 0
    ok = True

    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
        else:
            balance -= ans[idx]
            idx += 1

        if balance < 0:
            ok = False
            break

    if not ok or balance != 0:
        print(-1)
    else:
        print('\n'.join(map(str, ans)))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
