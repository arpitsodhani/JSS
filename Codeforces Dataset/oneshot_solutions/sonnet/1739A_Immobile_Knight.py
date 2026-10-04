import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        print(min(n, 2), min(m, 2))

if __name__ == "__main__":
    main()
