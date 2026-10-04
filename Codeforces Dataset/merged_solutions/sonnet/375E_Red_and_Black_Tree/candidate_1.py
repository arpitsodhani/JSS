# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

INF = 10 ** 30
NEG = -10 ** 18

def prune(states):
    if not states:
        return {}

    items = [(d, need, score) for (d, need), score in states.items()]
    needs = sorted({need for _, need, _ in items})
    pos = {v: i for i, v in enumerate(needs)}
    bit = [NEG] * (len(needs) + 1)

    def update(i, value):
        i += 1
        while i <= len(needs):
            if value > bit[i]:
                bit[i] = value
            i += i & -i

    def query(i):
        i += 1
        result = NEG
        while i > 0:
            if bit[i] > result:
                result = bit[i]
            i -= i & -i
        return result

    items.sort(key=lambda item: (item[0], item[1], -item[2]))
    result = {}

    for d, need, score in items:
        p = pos[need]
        if query(p) >= score:
            continue
        result[(d, need)] = score
        update(p, score)

    return result

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    idx = 0
    n = data[idx]
    x = data[idx + 1]
    idx += 2

    color = [0] + data[idx:idx + n]
    idx += n
    black_count = sum(color)

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = data[idx]
        b = data[idx + 1]
        w = data[idx + 2]
        idx += 3
        graph[a].append((b, w))
        graph[b].append((a, w))

    parent = [0] * (n + 1)
    order = [1]
    parent[1] = -1

    for v in order:
        for to, _ in graph[v]:
            if to != parent[v]:
                parent[to] = v
                order.append(to)

    dp = [None] * (n + 1)
    size = [0] * (n + 1)

    for v in reversed(order):
        limit = min(black_count, 1)
        cur = [{} for _ in range(limit + 1)]
        cur[0][(INF, 0)] = 0

        if black_count >= 1:
            cur[1][(0, -1)] = color[v]

        size[v] = 1

        for to, edge_len in graph[v]:
            if parent[to] != v:
                continue

            child = []
            for states in dp[to]:
                transformed = {}
                for (d, need), score in states.items():
                    nd = d + edge_len if d != INF and d + edge_len <= x else INF

                    if need == -1:
                        nn = -1
                    else:
                        nn = need + edge_len
                        if nn > x:
                            continue

                    key = (nd, nn)
                    if score > transformed.get(key, NEG):
                        transformed[key] = score

                child.append(transformed)

            new_limit = min(black_count, size[v] + size[to])
            new = [{} for _ in range(new_limit + 1)]

            for cnt1, states1 in enumerate(cur):
                if not states1:
                    continue

                for cnt2, states2 in enumerate(child):
                    if cnt1 + cnt2 > new_limit or not states2:
                        continue

                    dest = new[cnt1 + cnt2]

                    for (d1, need1), score1 in states1.items():
                        for (d2, need2), score2 in states2.items():
                            nd = d1 if d1 < d2 else d2

                            if need1 != -1 and (d2 == INF or need1 + d2 > x):
                                rem1 = need1
                            else:
                                rem1 = -1

                            if need2 != -1 and (d1 == INF or need2 + d1 > x):
                                rem2 = need2
                            else:
                                rem2 = -1

                            nn = rem1 if rem1 > rem2 else rem2
                            key = (nd, nn)
                            score = score1 + score2

                            if score > dest.get(key, NEG):
                                dest[key] = score

            cur = [prune(states) for states in new]
            size[v] += size[to]

        dp[v] = cur

    best = NEG
    if black_count < len(dp[1]):
        for (_, need), score in dp[1][black_count].items():
            if need == -1 and score > best:
                best = score

    print(-1 if best == NEG else black_count - best)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
