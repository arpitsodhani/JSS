import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        parity = [0] * k
        for i, c in enumerate(s):
            if c == '1':
                parity[i % k] ^= 1
        
        answers.append("YES" if all(x == 0 for x in parity) else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
