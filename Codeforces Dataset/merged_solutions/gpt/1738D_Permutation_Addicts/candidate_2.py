# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []
    sys.setrecursionlimit(300000)
    for _ in range(t):
        n = data[p]
        p += 1
        b = data[p:p + n]
        p += n
        k = 0
        children = [[] for _ in range(n + 2)]
        for i, x in enumerate(b, 1):
            v = x if x < i else i
            if v > k:
                k = v
            children[x].append(i)
        ans = []

        def dfs(u):
            if 1 <= u <= n:
                ans.append(u)
            heavy = []
            for v in children[u]:
                if children[v]:
                    heavy.append(v)
                else:
                    ans.append(v)
            for v in heavy:
                dfs(v)
        dfs(0)
        dfs(n + 1)
        out.append(str(k))
        out.append(' '.join(map(str, ans)))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
