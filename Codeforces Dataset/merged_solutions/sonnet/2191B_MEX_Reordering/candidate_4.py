# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    t = values[0]
    i = 1
    result = []

    for _ in range(t):
        n = values[i]
        i += 1
        part = values[i:i + n]
        i += n

        small = [0] * (n + 2)
        for x in part:
            if 0 <= x <= n + 1:
                small[x] += 1

        mex = 0
        while small[mex]:
            mex += 1

        ok = False
        if mex == 0:
            ok = n == 1
        else:
            j = 0
            while j < mex and not ok:
                ok = small[j] == 1
                j += 1

        result.append("YES" if ok else "NO")

    print("\n".join(result))

# CLAUSE: finish_program
main()
