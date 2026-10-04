import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        s = data[idx]
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        answer = 0
        i = 0
        
        while i < n:
            if s[i] == '1':
                total = 0
                while i < n and s[i] == '1':
                    total += a[i]
                    i += 1
                answer += total
            else:
                if i + 1 < n and s[i + 1] == '1':
                    total = a[i]
                    minimum = a[i]
                    i += 1
                    
                    while i < n and s[i] == '1':
                        total += a[i]
                        minimum = min(minimum, a[i])
                        i += 1
                    
                    answer += total - minimum
                else:
                    i += 1
        
        results.append(str(answer))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
