# CLAUSE: setup_environment
import sys

sys.setrecursionlimit(300000)

# CLAUSE: solve_logic
def main():
    def read_nonempty():
        line = sys.stdin.readline()
        while line is not None and line.strip() == "":
            line = sys.stdin.readline()
        return line

    def ask(k):
        if k in cache:
            return cache[k]
        print("?", k, flush=True)
        line = read_nonempty()
        if not line:
            cache[k] = []
            return []
        data = list(map(int, line.split()))
        if data[0] == 0:
            path = []
        else:
            path = data[1:]
        cache[k] = path
        return path

    def add_edge(u, v):
        if (u, v) in edges:
            return
        edges.add((u, v))
        left = []
        right = []
        for x in range(1, n + 1):
            if x == u or reach[x][u]:
                left.append(x)
            if x == v or reach[v][x]:
                right.append(x)
        for a in left:
            row = reach[a]
            for b in right:
                row[b] = True

    def can_continue(v, after):
        x = after + 1
        while x <= n:
            if x != v and not reach[x][v]:
                return True
            x += 1
        return False

    def has_prefix(path, prefix):
        return len(path) >= len(prefix) and path[:len(prefix)] == prefix

    def dfs(prefix, pos):
        v = prefix[-1]
        if done[v]:
            return count[v]
        total = 1
        query_pos = pos + 1
        last_child = 0
        while can_continue(v, last_child):
            path = ask(query_pos)
            if not has_prefix(path, prefix):
                count[v] = query_pos - pos
                done[v] = True
                return count[v]
            child = path[len(prefix)]
            add_edge(v, child)
            got = count[child] if done[child] else dfs(path, query_pos)
            total += got
            query_pos += got
            last_child = child
        count[v] = total
        done[v] = True
        return total

    first = read_nonempty()
    if not first:
        return
    tests = int(first)
    for _ in range(tests):
        line = read_nonempty()
        if not line:
            return
        n = int(line)
        cache = {}
        done = [False] * (n + 1)
        count = [0] * (n + 1)
        reach = [[False] * (n + 1) for _ in range(n + 1)]
        edges = set()
        pos = 1
        for v in range(1, n + 1):
            if done[v]:
                pos += count[v]
                continue
            path = ask(pos)
            if not path:
                break
            dfs(path, pos)
            pos += count[v]
        print("!", len(edges), flush=True)
        for u, v in edges:
            print(u, v, flush=True)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
