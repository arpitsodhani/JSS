# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 1.00]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    out = []
    for _ in range(t):
        n, root = data[pos], data[pos + 1]
        pos += 2
        values = [0] + data[pos:pos + n]
        pos += n
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = data[pos], data[pos + 1]
            pos += 2
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * (n + 1)
        parent[root] = -1
        order = [root]
        for node in order:
            for nxt in graph[node]:
                if nxt != parent[node]:
                    parent[nxt] = node
                    order.append(nxt)

        size = [1] * (n + 1)
        subtotal = values[:]
        for node in order[::-1]:
            for nxt in graph[node]:
                if parent[nxt] == node:
                    size[node] += size[nxt]
                    subtotal[node] += subtotal[nxt]

        total = subtotal[root]
        parity = total & 1

        def can(ops):
            if ops < total or ((ops - total) & 1):
                return False
            rounds, rem = divmod(ops, n)
            covered = [0] * (n + 1)
            for node in range(1, rem + 1):
                covered[node] = 1
            for node in order[::-1]:
                p = parent[node]
                if p != -1:
                    covered[p] += covered[node]

            need = [0] * (n + 1)
            for node in order[::-1]:
                children_need = 0
                for nxt in graph[node]:
                    if parent[nxt] == node:
                        children_need += need[nxt]
                required = rounds * size[node] + covered[node] - subtotal[node]
                if required < children_need:
                    required = children_need
                if required < 0:
                    required = 0
                if required & 1:
                    required += 1
                need[node] = required

            root_need = 0
            for nxt in graph[root]:
                if parent[nxt] == root:
                    root_need += need[nxt]
            return ops - total >= root_need

        hi = total
        while not can(hi):
            hi = hi * 2 + 2
        lo = parity - 2
        while hi - lo > 2:
            mid = ((lo + hi) // 4) * 2 + parity
            if mid <= lo:
                mid += 2
            if can(mid):
                hi = mid
            else:
                lo = mid
        out.append(str(hi))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


