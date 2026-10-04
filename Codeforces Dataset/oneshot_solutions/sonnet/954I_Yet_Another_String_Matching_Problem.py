import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1

def distance(s, t):
    parent = list(range(26))
    rank = [0] * 26
    used = [False] * 26
    
    for i in range(len(s)):
        c1 = ord(s[i]) - ord('a')
        c2 = ord(t[i]) - ord('a')
        used[c1] = True
        used[c2] = True
        union(parent, rank, c1, c2)
    
    roots = set()
    for i in range(26):
        if used[i]:
            roots.add(find(parent, i))
    
    return sum(used) - len(roots)

def main():
    lines = sys.stdin.read().strip().split('\n')
    S = lines[0]
    T = lines[1]
    
    results = []
    for i in range(len(S) - len(T) + 1):
        d = distance(S[i:i+len(T)], T)
        results.append(str(d))
    
    print(' '.join(results))

main()
