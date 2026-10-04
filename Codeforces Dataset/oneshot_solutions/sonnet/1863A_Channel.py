import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        a = int(data[idx + 1])
        q = int(data[idx + 2])
        s = data[idx + 3]
        idx += 4
        
        online = a
        max_online = a
        plus_count = 0
        
        for c in s:
            if c == '+':
                online += 1
                plus_count += 1
                max_online = max(max_online, online)
            else:
                online -= 1
        
        if a == n or max_online == n:
            results.append("YES")
        elif a + plus_count < n:
            results.append("NO")
        else:
            results.append("MAYBE")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
