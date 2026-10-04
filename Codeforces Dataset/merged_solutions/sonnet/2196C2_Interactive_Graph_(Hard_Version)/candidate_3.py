# CLAUSE: setup_environment
import sys

sys.setrecursionlimit(300000)

# CLAUSE: solve_logic
def main():
    def next_line():
        s = sys.stdin.readline()
        while s and s.strip() == "":
            s = sys.stdin.readline()
        return s

    def query(index):
        saved = asked.get(index)
        if saved is not None:
            return saved
        print("?", index, flush=True)
        s = next_line()
        if not s:
            result = []
        else:
            nums = list(map(int, s.split()))
            result = nums[1:] if nums[0] else []
        asked[index] = result
        return result

    def prefix_ok(a, b):
        if len(a) < len(b):
            return False
        for i, value in enumerate(b):
            if a[i] != value:
                return False
        return True

    def register(u, v):
        if (u, v) in edge_set:
            return
        edge_set.add((u, v))
        edge_list.append((u, v))
        target_bits = reach[v] | (1 << v)
        for a in range(1, n + 1):
            if a == u or ((reach[a] >> u) & 1):
                reach[a] |= target_bits

    def possible_child(v, last):
        for x in range(last + 1, n + 1):
            if x != v and ((reach[x] >> v) & 1) == 0:
                return True
        return False

    def walk(pref, start):
        root = pref[-1]
        if closed[root]:
            return ways[root]
        total = 1
        cur = start + 1
        last = 0
        while possible_child(root, last):
            p = query(cur)
            if not prefix_ok(p, pref):
                ways[root] = cur - start
                closed[root] = True
                return ways[root]
            child = p[len(pref)]
            register(root, child)
            size = ways[child] if closed[child] else walk(p, cur)
            total += size
            cur += size
            last = child
        ways[root] = total
        closed[root] = True
        return total

    line = next_line()
    if not line:
        return
    t = int(line)
    for _ in range(t):
        n_line = next_line()
        if not n_line:
            return
        n = int(n_line)
        asked = {}
        closed = [False] * (n + 1)
        ways = [0] * (n + 1)
        reach = [0] * (n + 1)
        edge_set = set()
        edge_list = []
        pos = 1
        vertex = 1
        while vertex <= n:
            if closed[vertex]:
                pos += ways[vertex]
                vertex += 1
                continue
            p = query(pos)
            if not p:
                break
            walk(p, pos)
            pos += ways[vertex]
            vertex += 1
        print("!", len(edge_list), flush=True)
        for u, v in edge_list:
            print(u, v, flush=True)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
