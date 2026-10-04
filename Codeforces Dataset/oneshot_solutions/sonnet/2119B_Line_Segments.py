import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        px, py, qx, qy = data[idx], data[idx + 1], data[idx + 2], data[idx + 3]
        idx += 4
        
        lengths = data[idx:idx + n]
        idx += n
        
        total = sum(lengths)
        longest = max(lengths)
        minimum = max(0, longest - (total - longest))
        
        dx = px - qx
        dy = py - qy
        dist_sq = dx * dx + dy * dy
        
        if minimum * minimum <= dist_sq <= total * total:
            answers.append("Yes")
        else:
            answers.append("No")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
