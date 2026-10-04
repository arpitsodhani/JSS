import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        current_time = 0
        current_side = 0
        answer = 0
        
        for _ in range(n):
            a = data[idx]
            b = data[idx + 1]
            idx += 2
            
            length = a - current_time
            need_parity = current_side ^ b
            
            if length % 2 == need_parity:
                answer += length
            else:
                answer += length - 1
            
            current_time = a
            current_side = b
        
        answer += m - current_time
        results.append(str(answer))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
