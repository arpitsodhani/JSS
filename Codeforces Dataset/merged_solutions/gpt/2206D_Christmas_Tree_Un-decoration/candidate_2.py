# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
NEG = -10 ** 30

class SegTree:
    __slots__ = ('n', 'a', 'b')

    def __init__(self, vals):
        m = len(vals)
        n = 1
        while n < m:
            n <<= 1
        self.n = n
        self.a = [NEG] * (2 * n)
        self.b = [0] * (2 * n)
        for i, (x, y) in enumerate(vals):
            self.a[n + i] = x
            self.b[n + i] = y
        for i in range(n - 1, 0, -1):
            la = self.a[i << 1]
            lb = self.b[i << 1]
            ra = self.a[i << 1 | 1]
            rb = self.b[i << 1 | 1]
            v = ra + lb
            self.a[i] = la if la >= v else v
            self.b[i] = lb + rb

    def update(self, pos, x, y):
        i = self.n + pos
        self.a[i] = x
        self.b[i] = y
        i >>= 1
        while i:
            la = self.a[i << 1]
            lb = self.b[i << 1]
            ra = self.a[i << 1 | 1]
            rb = self.b[i << 1 | 1]
            v = ra + lb
            self.a[i] = la if la >= v else v
            self.b[i] = lb + rb
            i >>= 1

    def value(self):
        return self.a[1] if self.a[1] >= self.b[1] else self.b[1]

def solve_case(n, q, parents, ornaments, queries):
    children = [[] for _ in range(n)]
    parent = [-1] * n
    for i, p in enumerate(parents, 1):
        p -= 1
        parent[i] = p
        children[p].append(i)
    order = [0]
    for v in order:
        order.extend(children[v])
    size = [1] * n
    heavy = [-1] * n
    dp = [0] * n
    for v in reversed(order):
        total = 0
        best_size = 0
        best_child = -1
        sz = 1
        for ch in children[v]:
            total += dp[ch]
            sz += size[ch]
            if size[ch] > best_size:
                best_size = size[ch]
                best_child = ch
        size[v] = sz
        heavy[v] = best_child
        dp[v] = ornaments[v] if ornaments[v] >= total else total
    light_sum = [0] * n
    for v in range(n):
        s = 0
        hv = heavy[v]
        for ch in children[v]:
            if ch != hv:
                s += dp[ch]
        light_sum[v] = s
    path_id = [-1] * n
    pos = [-1] * n
    heads = []
    paths = []
    starts = [0]
    for v in range(1, n):
        if heavy[parent[v]] != v:
            starts.append(v)
    for h in starts:
        pid = len(paths)
        heads.append(h)
        cur = h
        path = []
        while cur != -1:
            path_id[cur] = pid
            pos[cur] = len(path)
            path.append(cur)
            cur = heavy[cur]
        paths.append(path)
    segs = []
    path_val = []
    for path in paths:
        vals = [(ornaments[v], light_sum[v]) for v in path]
        st = SegTree(vals)
        segs.append(st)
        path_val.append(st.value())
    root_pid = path_id[0]
    out = [str(path_val[root_pid])]
    for u, x in queries:
        u -= 1
        ornaments[u] = x
        pid = path_id[u]
        old = path_val[pid]
        segs[pid].update(pos[u], x, light_sum[u])
        new = segs[pid].value()
        path_val[pid] = new
        delta = new - old
        h = heads[pid]
        while delta:
            if h == 0:
                break
            p = parent[h]
            light_sum[p] += delta
            pid = path_id[p]
            old = path_val[pid]
            segs[pid].update(pos[p], ornaments[p], light_sum[p])
            new = segs[pid].value()
            path_val[pid] = new
            delta = new - old
            h = heads[pid]
        out.append(str(path_val[root_pid]))
    return out

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        q = data[idx + 1]
        idx += 2
        parents = data[idx:idx + n - 1]
        idx += n - 1
        ornaments = data[idx:idx + n]
        idx += n
        queries = []
        for _ in range(q):
            u = data[idx]
            x = data[idx + 1]
            idx += 2
            queries.append((u, x))
        ans.extend(solve_case(n, q, parents, ornaments, queries))
    sys.stdout.write('\n'.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
