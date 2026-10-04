import sys

def ask(a, b, c):
    print(a, b, c, flush=True)
    res = input().strip()
    if res == "X":
        return (a, b)
    if res == "Y":
        return (b, c)
    return (c, a)

def build(leaves):
    if len(leaves) == 1:
        return leaves[0]
    if len(leaves) == 2:
        left = leaves[0]
        right = leaves[1]
        nodes.append((left, right))
        return len(nodes) + n
    
    a = leaves[0]
    b = leaves[1]
    
    same_a = [a]
    same_b = [b]
    
    for x in leaves[2:]:
        p = ask(a, b, x)
        if p == (a, x) or p == (x, a):
            same_a.append(x)
        elif p == (b, x) or p == (x, b):
            same_b.append(x)
        else:
            same_a.append(x)
    
    left = build(same_a)
    right = build(same_b)
    nodes.append((left, right))
    return len(nodes) + n

def main():
    global n, nodes
    
    n = int(input())
    nodes = []
    
    root = build(list(range(1, n + 1)))
    
    parent = [0] * (2 * n)
    for i, (u, v) in enumerate(nodes, start=n + 1):
        parent[u] = i
        parent[v] = i
    
    parent[root] = -1
    
    print(-1, flush=True)
    print(" ".join(map(str, parent[1:])), flush=True)

if __name__ == "__main__":
    main()
