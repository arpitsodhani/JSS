# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    n = data[0]
    used_h = set()
    used_v = set()
    ans = []

    idx = 1
    for day in range(1, n * n + 1):
        h = data[idx]
        v = data[idx + 1]
        idx += 2

        if h not in used_h and v not in used_v:
            used_h.add(h)
            used_v.add(v)
            ans.append(str(day))

    print(" ".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
