import sys

def possible_shift(p, n, m, shift):
    visited = [False] * n
    cycles = 0
    
    for i in range(n):
        if not visited[i]:
            cycles += 1
            v = i
            while not visited[v]:
                visited[v] = True
                v = (p[v] - 1 + shift) % n
    
    return n - cycles <= m

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        p = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        count = [0] * n
        for i, value in enumerate(p):
            shift = (i - (value - 1)) % n
            count[shift] += 1
        
        result = []
        need = n - 2 * m
        
        for shift in range(n):
            if count[shift] >= need and possible_shift(p, n, m, shift):
                result.append(shift)
        
        answers.append(str(len(result)) + (" " + " ".join(map(str, result)) if result else ""))
    
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()
