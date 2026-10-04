# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = (data[0], data[1])
    edges = []
    p = 2
    for i in range(m):
        w = data[p]
        in_tree = data[p + 1]
        p += 2
        edges.append((w, in_tree, i))
    order = sorted(edges, key=lambda x: (x[0], -x[1]))
    ans = [None] * m
    available = []
    tree_count = 0
    for w, in_tree, idx in order:
        if in_tree:
            tree_count += 1
            if tree_count >= n:
                print(-1)
                return
            u, v = (tree_count, tree_count + 1)
            ans[idx] = (u, v)
            for x in range(1, tree_count):
                available.append((x, v))
        else:
            if not available:
                print(-1)
                return
            ans[idx] = available.pop()
    if tree_count != n - 1:
        print(-1)
        return
    sys.stdout.write('\n'.join((f'{u} {v}' for u, v in ans)))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
