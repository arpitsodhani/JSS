# CLAUSE: setup_environment
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    result = []

# CLAUSE: solve_logic
    for _ in range(t):
        n = data[pos]
        pos += 1
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            a = data[pos]
            b = data[pos + 1]
            pos += 2
            graph[a].append(b)
            graph[b].append(a)

        parent = [0] * (n + 1)
        parent[n] = -1
        stack = [n]
        order = []

        while stack:
            node = stack.pop()
            order.append(node)
            for nxt in graph[node]:
                if nxt != parent[node]:
                    parent[nxt] = node
                    stack.append(nxt)

        on_path = [False] * (n + 1)
        node = 1
        while node != -1:
            on_path[node] = True
            if node == n:
                break
            node = parent[node]

        ans = []
        for node in order:
            if not on_path[node]:
                ans.append((2, node))
                ans.append((1, 0))

        node = 1
        while node != n:
            ans.append((2, node))
            ans.append((1, 0))
            node = parent[node]

        if ans and ans[-1][0] == 2:
            ans.pop()

        result.append(str(len(ans)))
        for typ, val in ans:
            if typ == 1:
                result.append("1")
            else:
                result.append("2 " + str(val))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
