import sys

def main():
    data = sys.stdin.read().split()
    
    if len(data) >= 2:
        n = int(data[0])
        x = int(data[1])
    else:
        s = data[0]
        n = int(s[:-1])
        x = int(s[-1])
    
    inverse = [
        [0, 1, 2],
        [1, 0, 2],
        [1, 2, 0],
        [2, 1, 0],
        [2, 0, 1],
        [1, 0, 2],
    ]
    
    print(inverse[n % 6][x])

if __name__ == "__main__":
    main()
