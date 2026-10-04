import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    results = []
    for case in range(1, t + 1):
        s = data[case]
        n = len(s)
        
        best = 0
        
        for d in "0123456789":
            best = max(best, s.count(d))
        
        for a in "0123456789":
            for b in "0123456789":
                if a == b:
                    continue
                
                length = 0
                need = a
                for c in s:
                    if c == need:
                        length += 1
                        need = b if need == a else a
                
                if length % 2 == 1:
                    length -= 1
                
                best = max(best, length)
        
        results.append(str(n - best))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
