import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        total = sum(a)
        
        best_gain = -4
        for i in range(n - 1):
            best_gain = max(best_gain, -2 * (a[i] + a[i + 1]))
        
        answers.append(str(total + best_gain))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
