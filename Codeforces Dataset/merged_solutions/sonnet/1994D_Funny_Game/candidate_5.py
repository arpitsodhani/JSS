# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_tree(n, values):
    parent = list(range(n))
    height = [1] * n

    def get(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    edges = []

    for step in range(n - 1, 0, -1):
        groups = [[] for _ in range(step)]
        selected = None

        for i in range(n):
            r = values[i] % step
            for j in groups[r]:
                a = get(i)
                b = get(j)
                if a != b:
                    if height[a] < height[b]:
                        a, b = b, a
                    parent[b] = a
                    height[a] += height[b]
                    selected = (i + 1, j + 1)
                    break
            if selected is not None:
                break
            groups[r].append(i)

        if selected is None:
            return None
        edges.append(selected)

    edges.reverse()
    return edges

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    t = data[at]
    at += 1
    ans = []

    for _ in range(t):
        n = data[at]
        at += 1
        values = data[at:at + n]
        at += n
        edges = build_tree(n, values)

        if edges is None:
            ans.append("NO")
            continue

        ans.append("YES")
        for u, v in edges:
            ans.append(str(u) + " " + str(v))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
