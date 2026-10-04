import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    a = data[idx:idx + n]
    idx += n
    
    s = data[idx]
    f = data[idx + 1]
    
    length = f - s
    doubled = a + a
    
    current = sum(doubled[:length])
    best_sum = current
    best_time = (s - 1) % n + 1
    
    for start in range(1, n):
        current += doubled[start + length - 1] - doubled[start - 1]
        time = (s - start - 1) % n + 1
        
        if current > best_sum or (current == best_sum and time < best_time):
            best_sum = current
            best_time = time
    
    print(best_time)

if __name__ == "__main__":
    main()
