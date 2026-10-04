import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n, x = data[0], data[1]
    a = data[2:]
    
    inf = n + 1
    first = [inf] * (x + 2)
    last = [0] * (x + 2)
    
    for i, v in enumerate(a, 1):
        if first[v] == inf:
            first[v] = i
        last[v] = i
    
    prefix_ok = [True] * (x + 2)
    max_last = 0
    for v in range(1, x + 1):
        prefix_ok[v] = prefix_ok[v - 1] and max_last <= first[v]
        max_last = max(max_last, last[v])
    
    suffix_ok = [True] * (x + 3)
    min_first = inf
    for v in range(x, 0, -1):
        suffix_ok[v] = suffix_ok[v + 1] and last[v] <= min_first
        min_first = min(min_first, first[v])
    
    prefix_last = [0] * (x + 2)
    for v in range(1, x + 1):
        prefix_last[v] = max(prefix_last[v - 1], last[v])
    
    suffix_first = [inf] * (x + 3)
    for v in range(x, 0, -1):
        suffix_first[v] = min(suffix_first[v + 1], first[v])
    
    result = 0
    r = 1
    
    for l in range(1, x + 1):
        if not prefix_ok[l - 1]:
            break
        
        if r < l:
            r = l
        
        while r <= x and (not suffix_ok[r + 1] or prefix_last[l - 1] > suffix_first[r + 1]):
            r += 1
        
        if r <= x:
            result += x - r + 1
    
    print(result)

if __name__ == "__main__":
    main()
