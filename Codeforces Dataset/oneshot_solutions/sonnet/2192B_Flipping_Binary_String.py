import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        
        ones = []
        zeros = []
        for i, c in enumerate(s, 1):
            if c == '1':
                ones.append(i)
            else:
                zeros.append(i)
        
        if len(ones) % 2 == 0:
            out.append(str(len(ones)))
            if ones:
                out.append(' '.join(map(str, ones)))
        elif len(zeros) % 2 == 1:
            out.append(str(len(zeros)))
            if zeros:
                out.append(' '.join(map(str, zeros)))
        else:
            out.append("-1")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
