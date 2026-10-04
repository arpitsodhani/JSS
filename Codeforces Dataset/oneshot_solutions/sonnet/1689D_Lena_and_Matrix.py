import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        max1 = max2 = max3 = max4 = -10**18
        
        for i in range(1, n + 1):
            row = data[idx]
            idx += 1
            
            for j, ch in enumerate(row, 1):
                if ch == 'B':
                    max1 = max(max1, i + j)
                    max2 = max(max2, i - j)
                    max3 = max(max3, -i + j)
                    max4 = max(max4, -i - j)
        
        best_dist = 10**18
        best_cell = (1, 1)
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dist = max(
                    max1 - (i + j),
                    max2 - (i - j),
                    max3 - (-i + j),
                    max4 - (-i - j)
                )
                
                if dist < best_dist:
                    best_dist = dist
                    best_cell = (i, j)
        
        answers.append(f"{best_cell[0]} {best_cell[1]}")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
