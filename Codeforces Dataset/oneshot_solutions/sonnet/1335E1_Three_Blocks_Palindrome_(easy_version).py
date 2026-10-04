import sys

def solve():
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
        
        values = sorted(set(a))
        comp = {v: i for i, v in enumerate(values)}
        m = len(values)
        arr = [comp[x] for x in a]
        
        positions = [[] for _ in range(m)]
        for i, x in enumerate(arr):
            positions[x].append(i)
        
        prefix = [[0] * m for _ in range(n + 1)]
        for i, x in enumerate(arr):
            prefix[i + 1] = prefix[i][:]
            prefix[i + 1][x] += 1
        
        best = 0
        for pos in positions:
            best = max(best, len(pos))
        
        for outer in range(m):
            cnt = len(positions[outer])
            for x in range(1, cnt // 2 + 1):
                left = positions[outer][x - 1]
                right = positions[outer][-x]
                
                middle = 0
                for val in range(m):
                    middle = max(middle, prefix[right][val] - prefix[left + 1][val])
                
                best = max(best, 2 * x + middle)
        
        answers.append(str(best))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    solve()
