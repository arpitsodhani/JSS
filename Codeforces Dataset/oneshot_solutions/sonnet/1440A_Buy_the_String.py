import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        c0 = int(data[idx + 1])
        c1 = int(data[idx + 2])
        h = int(data[idx + 3])
        s = data[idx + 4]
        idx += 5
        
        cost0 = min(c0, h + c1)
        cost1 = min(c1, h + c0)
        
        total = 0
        for ch in s:
            if ch == '0':
                total += cost0
            else:
                total += cost1
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
