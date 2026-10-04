# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        a = []
        for i in range(n):
            a.append((data[idx], i + 1))
            idx += 1
        
        a.sort()
        
        if n == 1:
            if m == 1:
                out.append("0")
            else:
                out.append("-1")
            continue
        
        if m == 0:
            total = sum(x for x, _ in a[:-1])
            if total < a[-1][0]:
                out.append("-1")
                continue
            
            suffix = 0
            j = n - 2
            while j >= 0:
                suffix += a[j][0]
                if suffix >= a[-1][0]:
                    break
                j -= 1
            
            ops = []
            for i in range(j):
                ops.append((a[i + 1][1], a[i][1]))
            
            strongest = a[-1][1]
            ops.append((strongest, a[j][1]))
            
            for i in range(j + 1, n - 1):
                ops.append((a[i][1], strongest))
            
            out.append(str(len(ops)))
            out.extend(f"{x} {y}" for x, y in ops)
        
        else:
            if m > n // 2:
                out.append("-1")
                continue
            
            ops = []
            for i in range(n - m):
                ops.append((a[i + m][1], a[i][1]))
            
            out.append(str(len(ops)))
            out.extend(f"{x} {y}" for x, y in ops)
    
    print("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
