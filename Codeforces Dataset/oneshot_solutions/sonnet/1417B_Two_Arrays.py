import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        target = int(data[idx + 1])
        idx += 2
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        half_count = 0
        colors = []
        
        for x in a:
            if 2 * x == target:
                colors.append(half_count % 2)
                half_count += 1
            elif 2 * x < target:
                colors.append(0)
            else:
                colors.append(1)
        
        answers.append(' '.join(map(str, colors)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
