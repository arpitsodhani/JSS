# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out_lines = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        p = data[idx:idx + n]
        idx += n

        pos = [0] * (n + 1)
        for i, x in enumerate(p):
            pos[x] = i

        ans = []
        r = n
        val = n

        while r > 0:
            while pos[val] >= r:
                val -= 1
            l = pos[val]
            ans.extend(p[l:r])
            r = l
            val -= 1

        out_lines.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
