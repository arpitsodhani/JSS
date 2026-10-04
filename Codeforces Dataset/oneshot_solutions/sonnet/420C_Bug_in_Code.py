import sys
from collections import defaultdict

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    p = data[1]
    
    degree = [0] * (n + 1)
    edges = defaultdict(int)
    
    idx = 2
    for _ in range(n):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        
        if a > b:
            a, b = b, a
        
        degree[a] += 1
        degree[b] += 1
        edges[(a, b)] += 1
    
    sorted_degree = sorted(degree[1:])
    
    answer = 0
    right = n - 1
    for left in range(n):
        while right > left and sorted_degree[left] + sorted_degree[right] >= p:
            right -= 1
        answer += n - max(right + 1, left + 1)
    
    for (a, b), cnt in edges.items():
        total = degree[a] + degree[b]
        if total >= p and total - cnt < p:
            answer -= 1
    
    print(answer)

if __name__ == "__main__":
    main()
