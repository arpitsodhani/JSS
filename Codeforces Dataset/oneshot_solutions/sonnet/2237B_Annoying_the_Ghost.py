import sys
from bisect import bisect_left

def solve_case(n, a, b):
    need = [bisect_left(b, x) + 1 for x in a]
    
    for x in need:
        if x > n:
            return -1
    
    used = [False] * (n + 1)
    assigned = [0] * n
    
    for i in range(n - 1, -1, -1):
        best = -1
        for j in range(n, need[i] - 1, -1):
            if not used[j]:
                best = j
                break
        
        if best == -1:
            return -1
        
        assigned[i] = best
        used[best] = True
    
    inversions = 0
    bit = [0] * (n + 1)
    
    def add(pos):
        while pos <= n:
            bit[pos] += 1
            pos += pos & -pos
    
    def get(pos):
        total = 0
        while pos > 0:
            total += bit[pos]
            pos -= pos & -pos
        return total
    
    for i, x in enumerate(assigned):
        inversions += i - get(x)
        add(x)
    
    return inversions

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        a = data[idx:idx + n]
        idx += n
        
        b = data[idx:idx + n]
        idx += n
        
        answers.append(str(solve_case(n, a, b)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
