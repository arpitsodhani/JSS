import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    vowels = "aeiou"
    out = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        base = n // 5
        extra = n % 5
        
        result = []
        for j, ch in enumerate(vowels):
            result.append(ch * (base + (1 if j < extra else 0)))
        
        out.append(''.join(result))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
