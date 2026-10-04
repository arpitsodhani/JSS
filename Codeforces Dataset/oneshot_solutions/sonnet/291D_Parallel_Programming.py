import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    
    if n == 1:
        out = []
        for _ in range(k):
            out.append("1")
        sys.stdout.write("\n".join(out))
        return
    
    need = n - 1
    if k < need.bit_length() - 1 + (1 if need & (need - 1) else 0):
        print(-1)
        return
    
    out = []
    prev_power = 1
    
    for _ in range(k):
        cur_power = min(need, prev_power * 2)
        row = []
        
        for i in range(1, n + 1):
            target = n - i
            before = min(target, prev_power)
            after = min(target, cur_power)
            add = after - before
            row.append(str(n - add))
        
        out.append(" ".join(row))
        prev_power = cur_power
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
