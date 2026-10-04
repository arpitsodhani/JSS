import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    
    for _ in range(t):
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        
        if x <= y:
            print(x, y)
        else:
            print(y, x)

if __name__ == "__main__":
    main()
