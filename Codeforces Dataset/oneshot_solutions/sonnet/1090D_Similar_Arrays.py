import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    total_pairs = n * (n - 1) // 2
    if n == 1 or m == total_pairs:
        print("NO")
        return
    
    graph = [set() for _ in range(n)]
    idx = 2
    for _ in range(m):
        a = int(data[idx]) - 1
        b = int(data[idx + 1]) - 1
        idx += 2
        graph[a].add(b)
        graph[b].add(a)
    
    u = v = -1
    for i in range(n):
        if len(graph[i]) < n - 1:
            u = i
            for j in range(n):
                if i != j and j not in graph[i]:
                    v = j
                    break
            break
    
    first = [0] * n
    second = [0] * n
    
    first[u] = 1
    first[v] = 2
    second[u] = 1
    second[v] = 1
    
    value = 3
    for i in range(n):
        if i == u or i == v:
            continue
        first[i] = value
        second[i] = value - 1
        value += 1
    
    print("YES")
    print(' '.join(map(str, first)))
    print(' '.join(map(str, second)))

if __name__ == "__main__":
    main()
