# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        ok = any(a[i] <= a[i + 1] for i in range(n - 1))
        ans.append("YES" if ok else "NO")

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
