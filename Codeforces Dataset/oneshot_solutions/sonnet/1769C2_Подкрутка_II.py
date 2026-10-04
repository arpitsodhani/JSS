import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    t = data[0]
    idx = 1
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        
        count = {}
        for x in a:
            count[x] = count.get(x, 0) + 1
        
        days = sorted(count)
        best = 0
        current = 0
        last_filled = -10**18
        
        for d in days:
            c = count[d]
            
            if c == 1:
                if last_filled == d - 1:
                    current += 1
                    last_filled = d
                elif last_filled == d:
                    current += 1
                    last_filled = d + 1
                else:
                    current = 1
                    last_filled = d
            else:
                start = d
                end = d + 1
                
                if last_filled >= d - 1:
                    current += end - max(last_filled, start - 1)
                else:
                    current = 2
                
                last_filled = end
            
            best = max(best, current)
        
        answers.append(str(best))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
