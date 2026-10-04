# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 1.00]
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    pos = 2
    edge = [[False] * n for _ in range(n)]
    for i in range(n):
        edge[i][i] = True
    for _ in range(m):
        u = int(data[pos]) - 1
        v = int(data[pos + 1]) - 1
        pos += 2
        edge[u][v] = True
        edge[v][u] = True

    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            v = queue.popleft()
            row = edge[v]
            for u in range(n):
                if u != v and not row[u]:
                    if color[u] == -1:
                        color[u] = color[v] ^ 1
                        queue.append(u)
                    elif color[u] == color[v]:
                        sys.stdout.write("No\n")
                        return

    ans = ["b"] * n
    for i in range(n):
        for j in range(n):
            if i != j and not edge[i][j]:
                ans[i] = "a" if color[i] == 0 else "c"
                break

    for i in range(n):
        for j in range(i + 1, n):
            need = not ((ans[i] == "a" and ans[j] == "c") or (ans[i] == "c" and ans[j] == "a"))
            if edge[i][j] != need:
                sys.stdout.write("No\n")
                return

    sys.stdout.write("Yes\n" + "".join(ans) + "\n")


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


