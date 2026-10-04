# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().split()
    if not data:
        sys.exit()

    t = int(data[0])
    ans = []

    for i in range(1, t + 1):
        s = data[i]
        ones = 0
        cost = 0
        for c in s:
            if c == '1':
                ones += 1
            elif ones:
                cost += ones + 1
        ans.append(str(cost))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
