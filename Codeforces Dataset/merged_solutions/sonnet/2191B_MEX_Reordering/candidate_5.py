# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def answer_case(a):
    n = len(a)
    exists = set()
    need = {}
    for x in a:
        exists.add(x)
        need[x] = need.get(x, 0) + 1

    mex = next(x for x in range(n + 2) if x not in exists)
    if mex == 0:
        return "YES" if n == 1 else "NO"

    singles = sum(1 for x in range(mex) if need.get(x, 0) == 1)
    return "YES" if singles > 0 else "NO"

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(it)
    lines = []
    for _ in range(t):
        n = next(it)
        a = [next(it) for _ in range(n)]
        lines.append(answer_case(a))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
