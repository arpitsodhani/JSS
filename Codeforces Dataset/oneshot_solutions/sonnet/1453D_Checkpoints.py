import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    answers = []
    
    for i in range(1, t + 1):
        k = int(data[i])
        
        if k % 2 == 1:
            answers.append("-1")
            continue
        
        k //= 2
        result = []
        
        while k > 0:
            length = k.bit_length() - 1
            result.extend([1] * length)
            k -= 1 << length
            
            if k > 0:
                result.append(0)
        
        answers.append(str(len(result)))
        answers.append(' '.join(map(str, result)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
