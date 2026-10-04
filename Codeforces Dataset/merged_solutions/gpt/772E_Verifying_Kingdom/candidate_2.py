# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    n_line = sys.stdin.readline().strip()
    if not n_line:
        return
    n = int(n_line)
    sys.setrecursionlimit(10000)
    max_id = 2 * n + 5
    parent = [0] * max_id
    children = {}
    rep = [0] * max_id
    for i in range(1, n + 1):
        rep[i] = i
    root = n + 1
    children[root] = [1, 2]
    parent[1] = root
    parent[2] = root
    rep[root] = 1
    current = [1, 2, root]
    nxt = n + 2

    def ask(a, b, c):
        print(a, b, c, flush=True)
        s = sys.stdin.readline().strip()
        if not s:
            sys.exit()
        if s[0] == '-':
            sys.exit()
        return s[0]
    for x in range(3, n + 1):
        candidates = current[:]
        while len(candidates) > 1:
            tin = [0] * max_id
            tout = [0] * max_id
            order = []
            timer = 0

            def dfs(u):
                nonlocal timer
                tin[u] = timer
                timer += 1
                order.append(u)
                if u in children:
                    dfs(children[u][0])
                    dfs(children[u][1])
                tout[u] = timer
            dfs(root)
            cnt = [0] * max_id
            for u in candidates:
                cnt[u] = 1
            for u in reversed(order):
                if u in children:
                    cnt[u] += cnt[children[u][0]] + cnt[children[u][1]]
            total = len(candidates)
            best = None
            best_val = total + 1
            for u in children:
                l, r = children[u]
                a = cnt[l]
                b = cnt[r]
                c = total - a - b
                val = max(a, b, c)
                if val < best_val:
                    best_val = val
                    best = u
            l, r = children[best]
            ans = ask(rep[l], rep[r], x)
            if ans == 'Z':
                candidates = [u for u in candidates if tin[l] <= tin[u] < tout[l]]
            elif ans == 'Y':
                candidates = [u for u in candidates if tin[r] <= tin[u] < tout[r]]
            else:
                candidates = [u for u in candidates if not tin[l] <= tin[u] < tout[l] and (not tin[r] <= tin[u] < tout[r])]
        edge_child = candidates[0]
        new_node = nxt
        nxt += 1
        old_parent = parent[edge_child]
        children[new_node] = [edge_child, x]
        rep[new_node] = rep[edge_child]
        parent[edge_child] = new_node
        parent[x] = new_node
        if old_parent == 0:
            root = new_node
            parent[new_node] = 0
        else:
            ch = children[old_parent]
            if ch[0] == edge_child:
                ch[0] = new_node
            else:
                ch[1] = new_node
            parent[new_node] = old_parent
        current.append(x)
        current.append(new_node)
    ans = [-1 if i == root else parent[i] for i in range(1, 2 * n)]
    print(-1, flush=True)
    print(*ans, flush=True)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
