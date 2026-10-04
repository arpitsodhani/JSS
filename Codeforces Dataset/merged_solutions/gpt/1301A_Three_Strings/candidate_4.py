# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit()

    t = int(data[0])
    idx = 1
    ans = []

    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        c = data[idx + 2]
        idx += 3

        ok = all(c[i] == a[i] or c[i] == b[i] for i in range(len(a)))
        ans.append("YES" if ok else "NO")

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
