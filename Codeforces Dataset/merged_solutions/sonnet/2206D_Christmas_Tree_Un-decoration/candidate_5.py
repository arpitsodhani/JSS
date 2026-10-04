# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    idx = 0
    cases = int(raw[idx])
    idx += 1
    lines = []

    for _ in range(cases):
        n = int(raw[idx])
        q = int(raw[idx + 1])
        idx += 2

        parent = [0] * (n + 1)
        child_count = [0] * (n + 1)
        bucket = defaultdict(list)
        for v in range(2, n + 1):
            p = int(raw[idx])
            idx += 1
            parent[v] = p
            child_count[p] += 1
            bucket[p].append(v)

        value = [0] * (n + 1)
        for v in range(1, n + 1):
            value[v] = int(raw[idx])
            idx += 1

        order = []
        stack = [1]
        while stack:
            v = stack.pop()
            order.append(v)
            stack += bucket[v]

        got = [0] * (n + 1)
        slack = [0] * (n + 1)
        for v in order[::-1]:
            total = 0
            for c in bucket[v]:
                total += got[c]
            if child_count[v] == 0:
                got[v] = value[v]
                slack[v] = value[v]
            elif value[v] > total:
                got[v] = value[v]
                slack[v] = value[v] - total
            else:
                got[v] = total

        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        node_at = [0] * (n + 1)
        time = 0
        stack = [(1, False)]
        while stack:
            v, exit_now = stack.pop()
            if exit_now:
                tout[v] = time
            else:
                time += 1
                tin[v] = time
                node_at[time] = v
                stack.append((v, True))
                for c in bucket[v][::-1]:
                    stack.append((c, False))

        parent_time = list(range(n + 1))
        active = [False] * (n + 1)

        def find(x):
            while parent_time[x] != x:
                parent_time[x] = parent_time[parent_time[x]]
                x = parent_time[x]
            return x

        for tpos in range(1, n + 1):
            v = node_at[tpos]
            if slack[v] > 0:
                active[tpos] = True
            else:
                parent_time[tpos] = tpos - 1

        answer = got[1]
        lines.append(str(answer))

        for _ in range(q):
            u = int(raw[idx])
            x = int(raw[idx + 1])
            idx += 2

            old = slack[u]
            fixed = value[u] - old
            new = x - fixed
            if new < 0:
                new = 0
            value[u] = x

            if new != old:
                slack[u] = new
                tpos = tin[u]
                if old == 0 and new > 0:
                    active[tpos] = True
                    parent_time[tpos] = tpos
                elif old > 0 and new == 0:
                    active[tpos] = False
                    parent_time[tpos] = find(tpos - 1)

                delta = new - old
                answer += delta

                if delta > 0:
                    p = find(tin[u])
                    while p and p >= tin[u] and tout[node_at[p]] >= tin[u] and delta:
                        v = node_at[p]
                        take = slack[v]
                        if take > delta:
                            take = delta
                        slack[v] -= take
                        answer -= take
                        delta -= take
                        if slack[v] == 0:
                            active[p] = False
                            parent_time[p] = find(p - 1)
                        p = find(p)

            lines.append(str(answer))

    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
