# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    ans = []
    for _ in range(t):
        n = next(it)
        q = next(it)
        parent = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        for v in range(2, n + 1):
            p = next(it)
            parent[v] = p
            children[p].append(v)
        perm = [0] + [next(it) for _ in range(n)]
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        timer = 0
        stack = [(1, 0)]
        while stack:
            v, state = stack.pop()
            if state == 0:
                timer += 1
                tin[v] = timer
                stack.append((v, 1))
                for u in reversed(children[v]):
                    stack.append((u, 0))
            else:
                tout[v] = timer

        def ok(i):
            v = perm[i]
            if v == 1:
                return i == 1
            if i == 1:
                return False
            pr = parent[v]
            prev = perm[i - 1]
            return tin[pr] <= tin[prev] <= tout[pr]
        good = 0
        for i in range(1, n + 1):
            good += ok(i)
        for _ in range(q):
            x = next(it)
            y = next(it)
            affected = {x, y}
            if x + 1 <= n:
                affected.add(x + 1)
            if y + 1 <= n:
                affected.add(y + 1)
            for i in affected:
                good -= ok(i)
            perm[x], perm[y] = (perm[y], perm[x])
            for i in affected:
                good += ok(i)
            ans.append('YES' if good == n else 'NO')
    sys.stdout.write('\n'.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
