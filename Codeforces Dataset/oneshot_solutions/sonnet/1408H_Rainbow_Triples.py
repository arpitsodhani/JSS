import sys

class SegTree:
    def __init__(self, n):
        self.n = n
        self.mx = [0] * (4 * n + 5)
        self.lazy = [0] * (4 * n + 5)
        self._build(1, 1, n)
    
    def _build(self, node, left, right):
        if left == right:
            self.mx[node] = left
            return
        
        mid = (left + right) // 2
        self._build(node * 2, left, mid)
        self._build(node * 2 + 1, mid + 1, right)
        self.mx[node] = max(self.mx[node * 2], self.mx[node * 2 + 1])
    
    def _apply(self, node, value):
        self.mx[node] += value
        self.lazy[node] += value
    
    def _push(self, node):
        if self.lazy[node]:
            value = self.lazy[node]
            self._apply(node * 2, value)
            self._apply(node * 2 + 1, value)
            self.lazy[node] = 0
    
    def add(self, ql, qr, value, node=1, left=1, right=None):
        if right is None:
            right = self.n
        
        if ql <= left and right <= qr:
            self._apply(node, value)
            return
        
        self._push(node)
        mid = (left + right) // 2
        
        if ql <= mid:
            self.add(ql, qr, value, node * 2, left, mid)
        if qr > mid:
            self.add(ql, qr, value, node * 2 + 1, mid + 1, right)
        
        self.mx[node] = max(self.mx[node * 2], self.mx[node * 2 + 1])
    
    def query(self, ql, qr, node=1, left=1, right=None):
        if right is None:
            right = self.n
        
        if ql <= left and right <= qr:
            return self.mx[node]
        
        self._push(node)
        mid = (left + right) // 2
        result = -10**18
        
        if ql <= mid:
            result = max(result, self.query(ql, qr, node * 2, left, mid))
        if qr > mid:
            result = max(result, self.query(ql, qr, node * 2 + 1, mid + 1, right))
        
        return result

def can_make(m, by_value, zero_count, color_count):
    if m == 0:
        return True
    if zero_count < 2 * m or color_count < m:
        return False
    
    starts = [[] for _ in range(m + 2)]
    
    for positions in by_value.values():
        prefix = 0
        suffix = m + 1
        has_middle = False
        
        for zeros_before in positions:
            if m <= zeros_before <= zero_count - m:
                has_middle = True
                break
            
            if zeros_before < m:
                prefix = max(prefix, zeros_before)
            elif zeros_before > zero_count - m:
                suffix = min(suffix, zeros_before - zero_count + m + 1)
        
        if has_middle:
            continue
        
        left = prefix + 1
        right = suffix - 1
        
        if left <= right:
            starts[left].append(right)
    
    seg = SegTree(m)
    
    for left in range(1, m + 1):
        for right in starts[left]:
            seg.add(1, right, 1)
        
        if seg.query(left, m) - left + 1 > color_count:
            return False
    
    return True

def solve_case(arr):
    zeros_before = 0
    by_value = {}
    
    for x in arr:
        if x == 0:
            zeros_before += 1
        else:
            by_value.setdefault(x, []).append(zeros_before)
    
    color_count = len(by_value)
    low = 0
    high = min(zeros_before // 2, color_count)
    
    while low < high:
        mid = (low + high + 1) // 2
        if can_make(mid, by_value, zeros_before, color_count):
            low = mid
        else:
            high = mid - 1
    
    return low

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        answers.append(str(solve_case(arr)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
