# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from bisect import bisect_right
from collections import deque

INF = 10**30

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    cards = []
    idx = 1
    
    for i in range(1, n + 1):
        a = data[idx]
        b = data[idx + 1]
        c = data[idx + 2]
        d = data[idx + 3]
        idx += 4
        cards.append((a, b, c, d, i))
    
    order = sorted(range(n), key=lambda i: cards[i][0])
    sorted_a = [cards[i][0] for i in order]
    
    size = 1
    while size < n:
        size *= 2
    
    tree = [INF] * (2 * size)
    for pos, card_idx in enumerate(order):
        tree[size + pos] = cards[card_idx][1]
    
    for i in range(size - 1, 0, -1):
        tree[i] = min(tree[2 * i], tree[2 * i + 1])
    
    def remove(pos):
        p = size + pos
        tree[p] = INF
        p //= 2
        while p:
            tree[p] = min(tree[2 * p], tree[2 * p + 1])
            p //= 2
    
    def find_available(limit, y):
        if limit < 0 or tree[1] > y:
            return -1
        
        def search(node, left, right):
            if left > limit or tree[node] > y:
                return -1
            if left == right:
                return left
            
            mid = (left + right) // 2
            res = search(node * 2, left, mid)
            if res != -1:
                return res
            return search(node * 2 + 1, mid + 1, right)
        
        return search(1, 0, size - 1)
    
    parent = [-1] * (n + 1)
    dist = [-1] * (n + 1)
    queue = deque()
    
    def add_reachable(x, y, from_card):
        limit = bisect_right(sorted_a, x) - 1
        
        while True:
            pos = find_available(limit, y)
            if pos == -1 or pos >= n:
                break
            
            card_idx = order[pos]
            original = cards[card_idx][4]
            parent[original] = from_card
            dist[original] = 1 if from_card == 0 else dist[from_card] + 1
            queue.append(original)
            remove(pos)
    
    add_reachable(0, 0, 0)
    
    while queue and dist[n] == -1:
        v = queue.popleft()
        _, _, x, y, _ = cards[v - 1]
        add_reachable(x, y, v)
    
    if dist[n] == -1:
        print(-1)
        return
    
    path = []
    cur = n
    while cur != 0:
        path.append(cur)
        cur = parent[cur]
    
    path.reverse()
    print(len(path))
    print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
