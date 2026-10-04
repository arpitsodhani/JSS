import sys

INF = 10 ** 18

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    a = data[idx:idx + n]
    idx += n
    
    queries = [[] for _ in range(n + 1)]
    for qi in range(m):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        queries[r].append((l, qi))
    
    size = 1
    while size < n:
        size *= 2
    
    tree = [INF] * (2 * size)
    
    def update(pos, value):
        pos += size - 1
        if value >= tree[pos]:
            return
        tree[pos] = value
        pos //= 2
        while pos:
            tree[pos] = min(tree[pos * 2], tree[pos * 2 + 1])
            pos //= 2
    
    def query(left, right):
        left += size - 1
        right += size - 1
        result = INF
        
        while left <= right:
            if left % 2 == 1:
                result = min(result, tree[left])
                left += 1
            if right % 2 == 0:
                result = min(result, tree[right])
                right -= 1
            left //= 2
            right //= 2
        
        return result
    
    last = {}
    answer = [-1] * m
    
    for i, value in enumerate(a, 1):
        if value in last:
            prev = last[value]
            update(prev, i - prev)
        last[value] = i
        
        for l, qi in queries[i]:
            best = query(l, i)
            if best != INF:
                answer[qi] = best
    
    sys.stdout.write('\n'.join(map(str, answer)))

if __name__ == "__main__":
    main()
