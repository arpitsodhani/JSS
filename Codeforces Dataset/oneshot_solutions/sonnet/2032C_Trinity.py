import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        a = data[idx:idx + n]
        idx += n
        a.sort()
        
        best = 2
        left = 0
        
        for right in range(2, n):
            while left + 1 < right and a[left] + a[left + 1] <= a[right]:
                left += 1
            best = max(best, right - left + 1)
        
        answers.append(str(n - best))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
