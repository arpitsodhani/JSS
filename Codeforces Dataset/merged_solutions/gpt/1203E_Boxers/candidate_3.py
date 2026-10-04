# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = sorted(data[1:])

    used = set()
    ans = 0

    for x in a:
        for y in (x - 1, x, x + 1):
            if y > 0 and y not in used:
                used.add(y)
                ans += 1
                break

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
