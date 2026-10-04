# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(it)
    answers = []
    for _ in range(t):
        n = next(it)
        x = next(it)
        value = [0]
        for _ in range(n):
            value.append(next(it))

        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = next(it)
            v = next(it)
            adj[u].append(v)
            adj[v].append(u)

        parent = [0] * (n + 1)
        parent[x] = -1
        children = [[] for _ in range(n + 1)]
        order = []
        stack = [x]
        while stack:
            v = stack.pop()
            order.append(v)
            for u in adj[v]:
                if u != parent[v]:
                    parent[u] = v
                    children[v].append(u)
                    stack.append(u)

        size = [0] * (n + 1)
        sub = [0] * (n + 1)
        for v in reversed(order):
            s = 1
            sm = value[v]
            for u in children[v]:
                s += size[u]
                sm += sub[u]
            size[v] = s
            sub[v] = sm

        total = sub[x]
        parity = total & 1

        def works(limit):
            if limit < total:
                return False
            spare = limit - total
            if spare & 1:
                return False

            q = limit // n
            r = limit - q * n
            cnt = [0] * (n + 1)
            for node in range(1, r + 1):
                cnt[node] = 1
            for v in reversed(order):
                add = cnt[v]
                if add and parent[v] != -1:
                    cnt[parent[v]] += add

            need = [0] * (n + 1)
            for v in reversed(order):
                from_children = 0
                for u in children[v]:
                    from_children += need[u]
                mandatory = q * size[v] + cnt[v] - sub[v]
                if mandatory < 0:
                    mandatory = 0
                if mandatory < from_children:
                    mandatory = from_children
                need[v] = mandatory if mandatory % 2 == 0 else mandatory + 1

            below_root = 0
            for u in children[x]:
                below_root += need[u]
            return spare >= below_root

        left = parity - 2
        right = total
        while not works(right):
            right = right + right + 2

        while right - left > 2:
            mid = (left + right) // 2
            if (mid & 1) != parity:
                mid += 1
            if mid <= left:
                mid += 2
            if mid >= right:
                mid -= 2
            if works(mid):
                right = mid
            else:
                left = mid

        answers.append(str(right))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
