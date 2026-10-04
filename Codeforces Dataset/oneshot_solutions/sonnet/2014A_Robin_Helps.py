import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        gold = 0
        helped = 0
        
        for _ in range(n):
            a = data[idx]
            idx += 1
            
            if a >= k:
                gold += a
            elif a == 0 and gold > 0:
                gold -= 1
                helped += 1
        
        answers.append(str(helped))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
