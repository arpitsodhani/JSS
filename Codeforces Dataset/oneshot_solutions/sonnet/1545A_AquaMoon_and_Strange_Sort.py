import sys
from collections import Counter

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
        
        sorted_a = sorted(a)
        
        even_initial = Counter()
        odd_initial = Counter()
        even_final = Counter()
        odd_final = Counter()
        
        for i in range(n):
            if i % 2 == 0:
                even_initial[a[i]] += 1
                even_final[sorted_a[i]] += 1
            else:
                odd_initial[a[i]] += 1
                odd_final[sorted_a[i]] += 1
        
        if even_initial == even_final and odd_initial == odd_final:
            answers.append("YES")
        else:
            answers.append("NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
