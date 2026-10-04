# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    v = list(map(int, input().split()))
    pref = []
    s = 0
    mx = 0
    for i, x in enumerate(v, 1):
        s += x
        pref.append(s)
        mx = max(mx, (s + i - 1) // i)

    q = int(input())
    ans = []
    for _ in range(q):
        t = int(input())
        if t < mx:
            ans.append("-1")
        else:
            ans.append(str((s + t - 1) // t))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
