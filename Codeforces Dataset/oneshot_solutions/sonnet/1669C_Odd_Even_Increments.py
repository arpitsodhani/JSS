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
        
        odd_parity = a[0] % 2
        even_parity = a[1] % 2 if n > 1 else -1
        
        possible = True
        for i in range(n):
            if i % 2 == 0:
                if a[i] % 2 != odd_parity:
                    possible = False
                    break
            else:
                if a[i] % 2 != even_parity:
                    possible = False
                    break
        
        answers.append("YES" if possible else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
