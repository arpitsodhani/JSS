import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    result = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        sequence = []
        
        for bit in range(61):
            if (n >> bit) & 1:
                value = n ^ (1 << bit)
                if value > 0:
                    sequence.append(value)
        
        sequence.append(n)
        sequence.sort()
        
        result.append(str(len(sequence)))
        result.append(' '.join(map(str, sequence)))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
