# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    import math

    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit()

    t = int(data[0])
    ans = []
    for i in range(1, t + 1):
        n = int(data[i])
        ans.append(f"{1 / math.tan(math.pi / (2 * n)):.9f}")

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
