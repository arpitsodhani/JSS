import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    idx = 1
    
    males = [0] * 367
    females = [0] * 367
    
    for _ in range(n):
        gender = data[idx]
        a = int(data[idx + 1])
        b = int(data[idx + 2])
        idx += 3
        
        days = males if gender == 'M' else females
        for d in range(a, b + 1):
            days[d] += 1
    
    answer = 0
    for d in range(1, 367):
        answer = max(answer, 2 * min(males[d], females[d]))
    
    print(answer)

if __name__ == "__main__":
    main()
