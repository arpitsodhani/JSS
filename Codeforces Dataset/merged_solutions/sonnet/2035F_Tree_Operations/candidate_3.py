# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    tests = nums[at]
    at += 1
    ans = []
    for _ in range(tests):
        n = nums[at]
        x = nums[at + 1]
        at += 2
        a = [0] + nums[at:at + n]
        at += n

        head = [-1] * (n + 1)
        to = [0] * (2 * max(0, n - 1))
        nxt = [0] * (2 * max(0, n - 1))
        edge = 0
        for _ in range(n - 1):
            u = nums[at]
            v = nums[at + 1]
            at += 2
            to[edge] = v
            nxt[edge] = head[u]
            head[u] = edge
            edge += 1
            to[edge] = u
            nxt[edge] = head[v]
            head[v] = edge
            edge += 1

        parent = [0] * (n + 1)
        parent[x] = -1
        order = []
        stack = [x]
        while stack:
            v = stack.pop()
            order.append(v)
            e = head[v]
            while e != -1:
                u = to[e]
                if u != parent[v]:
                    parent[u] = v
                    stack.append(u)
                e = nxt[e]

        size = [1] * (n + 1)
        sub = a[:]
        for v in reversed(order):
            e = head[v]
            while e != -1:
                u = to[e]
                if parent[u] == v:
                    size[v] += size[u]
                    sub[v] += sub[u]
                e = nxt[e]

        total = sub[x]
        want_parity = total & 1

        def ok(m):
            if m < total or (m - total) % 2:
                return False
            q, r = divmod(m, n)
            pref = [0] * (n + 1)
            for i in range(1, r + 1):
                pref[i] = 1
            for v in reversed(order):
                p = parent[v]
                if p > 0:
                    pref[p] += pref[v]

            need = [0] * (n + 1)
            for v in reversed(order):
                gathered = 0
                e = head[v]
                while e != -1:
                    u = to[e]
                    if parent[u] == v:
                        gathered += need[u]
                    e = nxt[e]
                base = q * size[v] + pref[v] - sub[v]
                if base < gathered:
                    base = gathered
                if base < 0:
                    base = 0
                need[v] = base + (base & 1)

            gathered = 0
            e = head[x]
            while e != -1:
                u = to[e]
                if parent[u] == x:
                    gathered += need[u]
                e = nxt[e]
            return m - total >= gathered

        lo = want_parity - 2
        hi = total
        while not ok(hi):
            hi = hi * 2 + 2
        while hi - lo > 2:
            middle = lo + ((hi - lo) // 4) * 2
            if (middle & 1) != want_parity:
                middle += 1
            if middle <= lo:
                middle += 2
            if ok(middle):
                hi = middle
            else:
                lo = middle
        ans.append(str(hi))
    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
main()
