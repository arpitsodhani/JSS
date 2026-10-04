import sys

def main():
    input = sys.stdin.readline

    n = int(input())
    color = list(map(int, input().split()))

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    total_red = color.count(1)
    total_blue = color.count(2)

    parent = [-1] * n
    order = [0]
    parent[0] = -2

    for v in order:
        for to in graph[v]:
            if to != parent[v]:
                parent[to] = v
                order.append(to)

    red = [0] * n
    blue = [0] * n
    ans = 0

    for v in reversed(order):
        if color[v] == 1:
            red[v] = 1
        elif color[v] == 2:
            blue[v] = 1

        for to in graph[v]:
            if parent[to] == v:
                red[v] += red[to]
                blue[v] += blue[to]

        if v != 0:
            if red[v] == total_red and blue[v] == 0:
                ans += 1
            elif blue[v] == total_blue and red[v] == 0:
                ans += 1

    print(ans)

if __name__ == "__main__":
    main()
