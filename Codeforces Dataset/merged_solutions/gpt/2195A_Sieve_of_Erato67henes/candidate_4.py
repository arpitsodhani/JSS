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
        arr = data[idx:idx + n]
        idx += n
        ans.append("YES" if 67 in arr else "NO")

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
