import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    q = int(data[idx + 2])
    idx += 3
    
    masks = [[0] * 26 for _ in range(m)]
    
    for row in range(n):
        s = data[idx]
        idx += 1
        bit = 1 << row
        for col, ch in enumerate(s):
            masks[col][ch - 97] |= bit
    
    answers = []
    
    for _ in range(q):
        query = data[idx]
        idx += 1
        
        good = masks[0][query[0] - 97]
        if good == 0:
            answers.append("-1")
            continue
        
        ops = 0
        possible = True
        
        for col in range(1, m):
            current = masks[col][query[col] - 97]
            if current == 0:
                possible = False
                break
            
            same = good & current
            if same:
                good = same
            else:
                ops += 1
                good = current
        
        answers.append(str(ops) if possible else "-1")
    
    print("\n".join(answers))

if __name__ == "__main__":
    main()
