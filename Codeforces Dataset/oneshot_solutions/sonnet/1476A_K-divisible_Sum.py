import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        total = ((n + k - 1) // k) * k
        answer = (total + n - 1) // n
        out.append(str(answer))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
