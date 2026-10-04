import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        total = 0
        values = []
        
        for i in range(1, n + 1):
            a = data[idx]
            idx += 1
            total += a
            values.append(a + i)
        
        values.sort(reverse=True)
        
        saved = sum(values[:k])
        damage = total + k * n - k * (k - 1) // 2 - saved
        answers.append(str(damage))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
