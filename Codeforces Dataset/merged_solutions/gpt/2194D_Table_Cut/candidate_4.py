# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        m = next(it)

        g = [[0] * m for _ in range(n)]
        total = 0
        for i in range(n):
            row = g[i]
            for j in range(m):
                x = next(it)
                row[j] = x
                total += x

        need = total // 2
        out.append(str(need * (total - need)))

        down_before_right = [0] * m
        got = 0

        for j in range(m - 1, -1, -1):
            c = 0
            for i in range(n):
                if got >= need:
                    break
                got += g[i][j]
                c += 1
            down_before_right[j] = c

        path = []
        r = 0
        for c in down_before_right:
            while r < c:
                path.append('D')
                r += 1
            path.append('R')
        while r < n:
            path.append('D')
            r += 1

        out.append(''.join(path))

    sys.stdout.write('\n'.join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
