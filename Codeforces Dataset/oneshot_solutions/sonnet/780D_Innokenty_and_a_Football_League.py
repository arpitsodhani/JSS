import sys
from collections import defaultdict, deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx])
    idx += 1
    
    first = []
    second = []
    by_first = defaultdict(list)
    
    for i in range(n):
        team = data[idx]
        city = data[idx + 1]
        idx += 2
        
        a = team[:3]
        b = team[:2] + city[0]
        first.append(a)
        second.append(b)
        by_first[a].append(i)
    
    use_second = [False] * n
    queue = deque()
    
    def force_group(code):
        for v in by_first.get(code, []):
            if not use_second[v]:
                use_second[v] = True
                queue.append(v)
    
    for code, clubs in by_first.items():
        if len(clubs) > 1:
            force_group(code)
    
    while queue:
        v = queue.popleft()
        force_group(second[v])
    
    used = set()
    answer = []
    
    for i in range(n):
        name = second[i] if use_second[i] else first[i]
        if name in used:
            print("NO")
            return
        used.add(name)
        answer.append(name)
    
    print("YES")
    print("\n".join(answer))

if __name__ == "__main__":
    main()
