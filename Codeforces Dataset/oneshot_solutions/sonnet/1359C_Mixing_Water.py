import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(q):
        h = int(data[idx])
        c = int(data[idx + 1])
        t = int(data[idx + 2])
        idx += 3
        
        if t >= h:
            answers.append("1")
            continue
        
        if 2 * t <= h + c:
            answers.append("2")
            continue
        
        down = 2 * t - h - c
        k = (h - t) // down
        
        candidates = {1, 2}
        for x in range(max(0, k - 2), k + 3):
            candidates.add(2 * x + 1)
        
        best = 1
        best_num = abs(h - t)
        best_den = 1
        
        for cups in candidates:
            hot = (cups + 1) // 2
            cold = cups // 2
            total = hot * h + cold * c
            
            num = abs(total - cups * t)
            den = cups
            
            if num * best_den < best_num * den:
                best = cups
                best_num = num
                best_den = den
            elif num * best_den == best_num * den and cups < best:
                best = cups
                best_num = num
                best_den = den
        
        answers.append(str(best))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
