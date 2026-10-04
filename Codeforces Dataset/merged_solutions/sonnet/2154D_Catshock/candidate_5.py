# CLAUSE: setup_environment
import sys

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    k = 0
    tests = values[k]
    k += 1
    lines = []

# CLAUSE: solve_logic
    for _ in range(tests):
        n = values[k]
        k += 1
        head = [-1] * (n + 1)
        to = [0] * (2 * max(0, n - 1))
        nxt = [0] * (2 * max(0, n - 1))
        edge = 0

        for _ in range(n - 1):
            a = values[k]
            b = values[k + 1]
            k += 2
            to[edge] = b
            nxt[edge] = head[a]
            head[a] = edge
            edge += 1
            to[edge] = a
            nxt[edge] = head[b]
            head[b] = edge
            edge += 1

        parent = [0] * (n + 1)
        parent[n] = -1
        stack = [n]
        order = []

        while stack:
            node = stack.pop()
            order.append(node)
            e = head[node]
            while e != -1:
                other = to[e]
                if other != parent[node]:
                    parent[other] = node
                    stack.append(other)
                e = nxt[e]

        path_mark = [0] * (n + 1)
        node = 1
        while node != -1:
            path_mark[node] = 1
            if node == n:
                break
            node = parent[node]

        commands = []
        for node in order:
            if path_mark[node] == 0:
                commands.append("2 " + str(node))
                commands.append("1")

        node = 1
        while node != n:
            commands.append("2 " + str(node))
            commands.append("1")
            node = parent[node]

        lines.append(str(len(commands)))
        lines.extend(commands)

# CLAUSE: finish_program
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
