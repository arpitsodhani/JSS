# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    s = sys.stdin.readline().strip()

    opening = set("(<[{")
    closing = set(")>]}")
    match = {')': '(', '>': '<', ']': '[', '}': '{'}

    stack = []
    ans = 0

    for ch in s:
        if ch in opening:
            stack.append(ch)
        else:
            if not stack:
                print("Impossible")
                sys.exit(0)
            top = stack.pop()
            if top != match[ch]:
                ans += 1

    if stack:
        print("Impossible")
    else:
        print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
