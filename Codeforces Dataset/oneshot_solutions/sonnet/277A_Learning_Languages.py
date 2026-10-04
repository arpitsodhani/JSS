import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    parent = list(range(n))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra
    
    first_employee = [-1] * (m + 1)
    knows_any = [False] * n
    
    for employee in range(n):
        k = data[idx]
        idx += 1
        
        if k > 0:
            knows_any[employee] = True
        
        for _ in range(k):
            lang = data[idx]
            idx += 1
            
            if first_employee[lang] == -1:
                first_employee[lang] = employee
            else:
                union(employee, first_employee[lang])
    
    zero_count = knows_any.count(False)
    
    components = set()
    for i in range(n):
        if knows_any[i]:
            components.add(find(i))
    
    if not components:
        print(n)
    else:
        print(len(components) - 1 + zero_count)

if __name__ == "__main__":
    main()
