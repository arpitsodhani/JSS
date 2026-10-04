import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        q = int(data[idx + 2])
        idx += 3
        
        current = 0
        answer = 0
        
        for _ in range(n):
            temp = int(data[idx])
            idx += 1
            
            if temp <= q:
                current += 1
            else:
                if current >= k:
                    length = current - k + 1
                    answer += length * (length + 1) // 2
                current = 0
        
        if current >= k:
            length = current - k + 1
            answer += length * (length + 1) // 2
        
        results.append(str(answer))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
