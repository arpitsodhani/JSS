# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from collections import Counter

    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]

    print("YES" if max(Counter(s).values(), default=0) <= k else "NO")

# CLAUSE: finish_program
def main():
    _inner_main()

main()
