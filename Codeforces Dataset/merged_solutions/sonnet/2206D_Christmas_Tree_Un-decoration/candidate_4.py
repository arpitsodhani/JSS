# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, i, v):
        n = self.n
        bit = self.bit
        while i <= n:
            bit[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        bit = self.bit
        while i:
            s += bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)
        bit = self.bit
        while step:
            nxt = idx + step
            if nxt <= self.n and bit[nxt] < k:
                idx = nxt
                k -= bit[nxt]
            step >>= 1
        return idx + 1

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    tc = data[ptr]
    ptr += 1
    res = []

    for _ in range(tc):
        n, q = data[ptr], data[ptr + 1]
        ptr += 2

        par = [0] * (n + 1)
        kids = [[] for _ in range(n + 1)]
        for i in range(2, n + 1):
            p = data[ptr]
            ptr += 1
            par[i] = p
            kids[p].append(i)

        ornaments = [0] + data[ptr:ptr + n]
        ptr += n

        traversal = [1]
        for v in traversal:
            for c in kids[v]:
                traversal.append(c)

        dp = [0] * (n + 1)
        spare = [0] * (n + 1)
        for v in reversed(traversal):
            children_sum = 0
            for c in kids[v]:
                children_sum += dp[c]
            spare[v] = ornaments[v] - children_sum
            if spare[v] < 0:
                spare[v] = 0
            dp[v] = children_sum + spare[v]

        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        rev = [0] * (n + 1)
        tick = 0
        st = [(1, 0)]
        while st:
            v, state = st.pop()
            if state:
                tout[v] = tick
            else:
                tick += 1
                tin[v] = tick
                rev[tick] = v
                st.append((v, 1))
                for c in reversed(kids[v]):
                    st.append((c, 0))

        fw = Fenwick(n)
        for v in range(1, n + 1):
            if spare[v] > 0:
                fw.add(tin[v], 1)

        ans = dp[1]
        res.append(str(ans))

        for _ in range(q):
            u, x = data[ptr], data[ptr + 1]
            ptr += 2

            before = spare[u]
            without_spare = ornaments[u] - before
            after = x - without_spare
            if after < 0:
                after = 0
            ornaments[u] = x

            if before != after:
                spare[u] = after
                if before == 0:
                    fw.add(tin[u], 1)
                elif after == 0:
                    fw.add(tin[u], -1)

                delta = after - before
                ans += delta

                while delta > 0:
                    count = fw.sum(tin[u])
                    if count == 0:
                        break
                    pos = fw.kth(count)
                    v = rev[pos]
                    if tout[v] < tin[u]:
                        break

                    take = spare[v]
                    if take > delta:
                        take = delta
                    spare[v] -= take
                    ans -= take
                    delta -= take
                    if spare[v] == 0:
                        fw.add(pos, -1)

            res.append(str(ans))

    sys.stdout.write("\n".join(res))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
