# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]

    r = s.count('R')
    g = s.count('G')
    b = s.count('B')

    seen = {(r, g, b)}
    stack = [(r, g, b)]
    ans = set()

    while stack:
        r, g, b = stack.pop()
        if r + g + b == 1:
            if r:
                ans.add('R')
            if g:
                ans.add('G')
            if b:
                ans.add('B')
            continue

        nxt = []
        if r >= 2:
            nxt.append((r - 1, g, b))
        if g >= 2:
            nxt.append((r, g - 1, b))
        if b >= 2:
            nxt.append((r, g, b - 1))
        if r and g:
            nxt.append((r - 1, g - 1, b + 1))
        if r and b:
            nxt.append((r - 1, g + 1, b - 1))
        if g and b:
            nxt.append((r + 1, g - 1, b - 1))

        for state in nxt:
            if state not in seen:
                seen.add(state)
                stack.append(state)

    print(''.join(c for c in 'BGR' if c in ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
