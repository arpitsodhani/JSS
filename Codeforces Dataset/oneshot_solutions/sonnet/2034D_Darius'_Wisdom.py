import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        
        count0 = a.count(0)
        count1 = a.count(1)
        mid_end = count0 + count1
        
        moves = []
        one_pos = {i for i, x in enumerate(a) if x == 1}
        zero_outside = {i for i, x in enumerate(a) if x == 0 and i >= count0}
        
        def swap(i, j):
            for p in (i, j):
                if a[p] == 1:
                    one_pos.discard(p)
                if p >= count0 and a[p] == 0:
                    zero_outside.discard(p)
            
            if a[i] > a[j]:
                moves.append((i + 1, j + 1))
            else:
                moves.append((j + 1, i + 1))
            
            a[i], a[j] = a[j], a[i]
            
            for p in (i, j):
                if a[p] == 1:
                    one_pos.add(p)
                if p >= count0 and a[p] == 0:
                    zero_outside.add(p)
        
        for i in range(count0):
            if a[i] == 0:
                continue
            
            j = next(iter(zero_outside))
            
            if a[i] == 1:
                swap(i, j)
            else:
                p = next(iter(one_pos))
                swap(i, p)
                swap(i, j)
        
        one_right = {i for i in range(mid_end, n) if a[i] == 1}
        
        for i in range(count0, mid_end):
            if a[i] == 2:
                j = one_right.pop()
                swap(i, j)
        
        out.append(str(len(moves)))
        for u, v in moves:
            out.append(f"{u} {v}")
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
