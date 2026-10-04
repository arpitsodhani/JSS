import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        pins = []
        for _ in range(n):
            pins.append(data[idx])
            idx += 1
        
        used = set()
        duplicates = []
        
        for i in range(n):
            if pins[i] in used:
                duplicates.append(i)
            else:
                used.add(pins[i])
        
        changes = 0
        
        for i in duplicates:
            s = list(pins[i])
            found = False
            
            for pos in range(4):
                old = s[pos]
                for digit in "0123456789":
                    if digit == old:
                        continue
                    
                    s[pos] = digit
                    candidate = ''.join(s)
                    
                    if candidate not in used:
                        pins[i] = candidate
                        used.add(candidate)
                        changes += 1
                        found = True
                        break
                
                if found:
                    break
                s[pos] = old
        
        out.append(str(changes))
        out.extend(pins)
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
