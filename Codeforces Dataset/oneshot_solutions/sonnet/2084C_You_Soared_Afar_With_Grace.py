import sys

def solve_case(n, a, b):
    pos_a = [0] * (n + 1)
    for i, x in enumerate(a):
        pos_a[x] = i
    
    used = [False] * n
    loops = []
    pairs = []
    
    for i in range(n):
        if used[i]:
            continue
        
        x, y = a[i], b[i]
        if x == y:
            used[i] = True
            loops.append(i)
        else:
            j = pos_a[y]
            if b[j] != x or i == j:
                return None
            used[i] = used[j] = True
            pairs.append((i, j))
    
    if len(loops) != n % 2:
        return None
    
    target = [0] * n
    left, right = 0, n - 1
    
    for i, j in pairs:
        target[left] = i
        target[right] = j
        left += 1
        right -= 1
    
    if loops:
        target[left] = loops[0]
    
    current = list(range(n))
    position = list(range(n))
    operations = []
    
    for i in range(n):
        need = target[i]
        if current[i] == need:
            continue
        
        j = position[need]
        current[i], current[j] = current[j], current[i]
        position[current[i]] = i
        position[current[j]] = j
        operations.append((i + 1, j + 1))
    
    return operations

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        b = list(map(int, data[idx:idx + n]))
        idx += n
        
        operations = solve_case(n, a, b)
        
        if operations is None:
            out.append("-1")
        else:
            out.append(str(len(operations)))
            for i, j in operations:
                out.append(f"{i} {j}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
