# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    s = data[idx]
    idx += 1
    n = len(s)
    
    m = int(data[idx])
    idx += 1
    
    full = (1 << 6) - 1
    allowed = [full] * n
    
    for _ in range(m):
        pos = int(data[idx]) - 1
        letters = data[idx + 1]
        idx += 2
        
        mask = 0
        for ch in letters:
            mask |= 1 << (ord(ch) - ord('a'))
        allowed[pos] = mask
    
    counts = [0] * 6
    for ch in s:
        counts[ord(ch) - ord('a')] += 1
    
    need = [0] * 64
    for mask in allowed:
        need[mask] += 1
    
    subsets = [[] for _ in range(64)]
    for mask in range(64):
        for sub in range(64):
            if sub & ~mask == 0:
                subsets[mask].append(sub)
    
    def possible():
        cap = [0] * 64
        for mask in range(1, 64):
            total = 0
            for c in range(6):
                if (mask >> c) & 1:
                    total += counts[c]
            cap[mask] = total
        
        for mask in range(1, 64):
            positions = 0
            for sub in subsets[mask]:
                positions += need[sub]
            if positions > cap[mask]:
                return False
        return True
    
    if not possible():
        print("Impossible")
        return
    
    result = []
    
    for i in range(n):
        mask = allowed[i]
        need[mask] -= 1
        
        placed = False
        for c in range(6):
            if ((mask >> c) & 1) and counts[c] > 0:
                counts[c] -= 1
                if possible():
                    result.append(chr(ord('a') + c))
                    placed = True
                    break
                counts[c] += 1
        
        if not placed:
            print("Impossible")
            return
    
    print(''.join(result))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
