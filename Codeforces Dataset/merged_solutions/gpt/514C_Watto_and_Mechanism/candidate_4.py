# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.buffer.read().split()
    if not data:
        sys.exit()

    n = int(data[0])
    m = int(data[1])
    words = data[2:2 + n]
    queries = data[2 + n:2 + n + m]

    nexts = [[-1, -1, -1]]
    end = [False]

    for w in words:
        v = 0
        for ch in w:
            c = ch - 97
            u = nexts[v][c]
            if u == -1:
                u = len(nexts)
                nexts[v][c] = u
                nexts.append([-1, -1, -1])
                end.append(False)
            v = u
        end[v] = True

    ans = []

    for s in queries:
        stack = [(0, 0, 0)]
        ok = False
        L = len(s)

        while stack and not ok:
            v, i, diff = stack.pop()

            if i == L:
                if diff == 1 and end[v]:
                    ok = True
                continue

            c = s[i] - 97

            if diff == 1:
                u = nexts[v][c]
                if u != -1:
                    stack.append((u, i + 1, 1))
            else:
                row = nexts[v]
                for nc in range(3):
                    u = row[nc]
                    if u != -1:
                        stack.append((u, i + 1, nc != c))

        ans.append("YES" if ok else "NO")

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
