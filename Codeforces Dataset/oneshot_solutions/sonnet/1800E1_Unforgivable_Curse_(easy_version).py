import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        s = data[idx + 2]
        target = data[idx + 3]
        idx += 4
        
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
        
        for i in range(n):
            if i + k < n:
                union(i, i + k)
            if i + k + 1 < n:
                union(i, i + k + 1)
        
        counts = defaultdict(lambda: [0] * 26)
        
        for i in range(n):
            root = find(i)
            counts[root][ord(s[i]) - 97] += 1
            counts[root][ord(target[i]) - 97] -= 1
        
        possible = True
        for count in counts.values():
            if any(x != 0 for x in count):
                possible = False
                break
        
        answers.append("YES" if possible else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
