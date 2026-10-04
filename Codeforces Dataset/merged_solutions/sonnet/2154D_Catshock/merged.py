# Clause setup_environment [Confidence: 0.40]
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    result = []


# Clause solve_logic [Confidence: 0.40]
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


# Clause finish_program [Confidence: 0.40]
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()


