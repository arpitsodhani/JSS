# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    n = data[at]
    m = data[at + 1]
    at += 2
    a = [0] + data[at:at + n]
    at += n
    b = [0] + data[at:at + n]
    at += n

    ops = []
    query_count = 0
    for _ in range(m):
        typ = data[at]
        at += 1
        if typ == 1:
            x = data[at]
            y = data[at + 1]
            k = data[at + 2]
            at += 3
            ops.append((1, x, y, k))
        else:
            pos = data[at]
            at += 1
            ops.append((2, pos, query_count, 0))
            query_count += 1

    waiting = defaultdict(list)
    parent = list(range(n + 2))
    active = [False] * (n + 2)
    answer = [0] * query_count

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for op in reversed(ops):
        if op[0] == 2:
            pos = op[1]
            qid = op[2]
            waiting[pos].append(qid)
            if not active[pos]:
                active[pos] = True
                parent[pos] = pos
        else:
            x = op[1]
            y = op[2]
            k = op[3]
            end = y + k - 1
            pos = find(y)
            while pos <= end:
                for qid in waiting[pos]:
                    answer[qid] = a[x + pos - y]
                waiting[pos].clear()
                active[pos] = False
                parent[pos] = find(pos + 1)
                pos = parent[pos]

    for pos, ids in waiting.items():
        for qid in ids:
            answer[qid] = b[pos]

    sys.stdout.write("\n".join(map(str, answer)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
