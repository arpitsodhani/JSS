# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        x = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n

        first = -1
        last = -1
        for i, v in enumerate(a):
            if v == 1:
                if first == -1:
                    first = i
                last = i

        if first == -1 or last - first + 1 <= x:
            ans.append("YES")
        else:
            ans.append("NO")

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
