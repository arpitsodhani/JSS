import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    m = data[1]
    idx = 2
    
    parent = list(range(n + 2))
    answer = [0] * (n + 1)
    
    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    
    for _ in range(m):
        l = data[idx]
        r = data[idx + 1]
        x = data[idx + 2]
        idx += 3
        
        v = find(l)
        while v <= r:
            if v == x:
                v = find(v + 1)
            else:
                answer[v] = x
                parent[v] = find(v + 1)
                v = find(v)
    
    print(' '.join(map(str, answer[1:])))

if __name__ == "__main__":
    main()
