# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    import re

    data = sys.stdin.read()
    tokens = re.findall(r'\d+|left|right', data)

    n = int(tokens[0])
    m = int(tokens[1])

    l, r = 1, n
    i = 2

    for _ in range(m):
        direction = tokens[i]
        x = int(tokens[i + 1])
        i += 2

        if direction == "left":
            r = min(r, x - 1)
        else:
            l = max(l, x + 1)

    print(r - l + 1 if l <= r else -1)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
