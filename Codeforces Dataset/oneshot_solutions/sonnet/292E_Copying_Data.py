import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    a = [0] + data[idx:idx + n]
    idx += n
    
    b = [0] + data[idx:idx + n]
    idx += n
    
    size = 4 * n + 5
    lazy_time = [0] * size
    lazy_shift = [0] * size
    
    def update(node, left, right, ql, qr, shift, tm):
        if ql <= left and right <= qr:
            lazy_time[node] = tm
            lazy_shift[node] = shift
            return
        
        mid = (left + right) // 2
        if ql <= mid:
            update(node * 2, left, mid, ql, qr, shift, tm)
        if qr > mid:
            update(node * 2 + 1, mid + 1, right, ql, qr, shift, tm)
    
    def query(node, left, right, pos):
        best_time = lazy_time[node]
        best_shift = lazy_shift[node]
        
        while left != right:
            mid = (left + right) // 2
            if pos <= mid:
                node = node * 2
                right = mid
            else:
                node = node * 2 + 1
                left = mid + 1
            
            if lazy_time[node] > best_time:
                best_time = lazy_time[node]
                best_shift = lazy_shift[node]
        
        if best_time == 0:
            return b[pos]
        return a[pos + best_shift]
    
    out = []
    for tm in range(1, m + 1):
        typ = data[idx]
        idx += 1
        
        if typ == 1:
            x = data[idx]
            y = data[idx + 1]
            k = data[idx + 2]
            idx += 3
            update(1, 1, n, y, y + k - 1, x - y, tm)
        else:
            pos = data[idx]
            idx += 1
            out.append(str(query(1, 1, n, pos)))
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
