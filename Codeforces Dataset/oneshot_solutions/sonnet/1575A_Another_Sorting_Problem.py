import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    books = []
    for i in range(n):
        s = data[i + 2]
        key = []
        for j, c in enumerate(s):
            if j % 2 == 0:
                key.append(c)
            else:
                key.append(chr(255 - ord(c)))
        books.append((''.join(key), i + 1))
    
    books.sort()
    print(' '.join(str(idx) for _, idx in books))

if __name__ == "__main__":
    main()
