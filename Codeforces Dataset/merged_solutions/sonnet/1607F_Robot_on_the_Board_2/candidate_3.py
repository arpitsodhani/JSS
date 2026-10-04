# CLAUSE: setup_environment
import sys
from collections import deque

def main():
    tokens = sys.stdin.buffer.read().split()
    q = 0
    tc = int(tokens[q])
    q += 1
    output = []

# CLAUSE: solve_logic
    for _ in range(tc):
        n = int(tokens[q])
        m = int(tokens[q + 1])
        q += 2
        grid = tokens[q:q + n]
        q += n
        total = n * m
        to = [-1] * total
        indeg = [0] * total
        head = [-1] * total
        link = [-1] * total

        for i in range(n):
            row = grid[i]
            base = i * m
            for j in range(m):
                v = base + j
                ch = row[j]
                if ch == 76:
                    u = v - 1 if j else -1
                elif ch == 82:
                    u = v + 1 if j + 1 < m else -1
                elif ch == 85:
                    u = v - m if i else -1
                else:
                    u = v + m if i + 1 < n else -1
                to[v] = u
                if u != -1:
                    indeg[u] += 1
                    link[v] = head[u]
                    head[u] = v

        alive = bytearray(b"\x01") * total
        dq = deque(i for i in range(total) if indeg[i] == 0)
        order = []
        while dq:
            v = dq.popleft()
            alive[v] = 0
            order.append(v)
            u = to[v]
            if u != -1:
                indeg[u] -= 1
                if indeg[u] == 0:
                    dq.append(u)

        dist = [0] * total
        seen = bytearray(total)
        for i in range(total):
            if alive[i] and not seen[i]:
                cyc = []
                v = i
                while not seen[v]:
                    seen[v] = 1
                    cyc.append(v)
                    v = to[v]
                size = len(cyc)
                for v in cyc:
                    dist[v] = size

        for v in reversed(order):
            u = to[v]
            if u == -1:
                dist[v] = 1
            else:
                dist[v] = dist[u] + 1

        best = 0
        cell = 0
        for i, val in enumerate(dist):
            if val > best:
                best = val
                cell = i
        output.append(f"{cell // m + 1} {cell % m + 1} {best}")

# CLAUSE: finish_program
    print("\n".join(output))

if __name__ == "__main__":
    main()
